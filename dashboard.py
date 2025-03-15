import streamlit as st
import requests
import time
from threading import Thread
import pandas as pd 



class ServerDisplay(Thread):
	def __init__(self,webpage_link):
		super().__init__()
		self.webpage_link=webpage_link
		self.cpu=0
		self.memory = 0
		self.disk = 0
		self.IO =0

	def run(self):
		"""Run the thread"""
		while True:
			self.fetch_stats()
			time.sleep(2)

	def fetch_stats(self):
		"""Fetch server stats from API"""
		response = requests.get(self.webpage_link)
		
		data = response.json()
		print(data)
		self.cpu = data["CPU"]
		self.memory = data["Memory"]
		self.disk = data["HDD (Disk)"]
		self.IO
		
class TabClass:
	def __init__(self,thread):
		self.server_display=thread
		self.error_placeholder=st.empty()
		self.cpu_placeholder = st.empty()
		self.memory_placeholder = st.empty()
		self.disk_placeholder = st.empty()
		self.line_chart_placeholder=st.empty()
		self.cpu_data=[]
		self.memory_data=[]
		self.disk_data=[]
		self.timestamps=[]
	def update_tab(self):
		if (self.server_display.cpu,self.server_display.memory,self.server_display.disk)==(0,0,0):
			self.error_placeholder.subheader("No connection")
			return
		timestamp = time.strftime('%H:%M:%S')
		self.cpu_data.append(self.server_display.cpu)
		self.memory_data.append(self.server_display.memory)
		self.disk_data.append(self.server_display.disk)
		self.timestamps.append(timestamp)
		data = {
			"Timestamp": self.timestamps,
			"CPU (%)": self.cpu_data,
			"Memory (%)": self.memory_data,
			"Disk (%)": self.disk_data,
		}
		stats_df = pd.DataFrame(data)
		self.line_chart_placeholder.line_chart(stats_df,x='Timestamp',y=['CPU (%)',"Memory (%)","Disk (%)"])
		self.cpu_placeholder.metric("CPU Usage", f"{self.server_display.cpu}%")
		self.memory_placeholder.metric("Memory Usage", f"{self.server_display.memory}%")
		self.disk_placeholder.metric("Disk Usage", f"{self.server_display.disk}%")
	
def main():
	st.title("Linux Monitoring Dashboard")
	tab1, tab2, tab3 = st.tabs(["Server1", "Server2", "Server3"])
	#make threads to fetch api data from different servers
	server_display1=ServerDisplay("http://35.231.107.155:5000/stats")
	server_display1.start()
	server_display2=ServerDisplay("http://34.133.20.113:5000/stats")
	server_display2.start()
	server_display3=ServerDisplay("ip_here")
	server_display3.start()
	

	cpu_data2=[]
	memory_data2=[]
	disk_data2=[]
	timestamps2=[]
	with tab1:
		tab1_update_class=TabClass(server_display1)
	with tab2:
		tab2_update_class=TabClass(server_display2)
	with tab3:
		tab3_update_class=TabClass(server_display3)
	
	while True:
		#this is the logic loop that calls updates
		tab1_update_class.update_tab()
		tab2_update_class.update_tab()
		time.sleep(2)

if __name__ == '__main__':
	main()