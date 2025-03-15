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

	def run(self):
		"""Run the thread"""
		while True:
			self.fetch_stats()
			time.sleep(2)

	def fetch_stats(self):
		"""Fetch server stats from API"""
		response = requests.get(self.webpage_link)
		data = response.json()
		self.cpu = data["CPU"]
		self.memory = data["Memory"]
		self.disk = data["HDD (Disk)"]
		
		
	
def main():
	st.title("Linux Monitoring Dashboard")
	tab1, tab2, tab3 = st.tabs(["Server1", "Server2", "Server3"])
	#make threads to fetch api data from different servers
	server_display1=ServerDisplay("http://35.231.107.155:5000/stats")
	server_display1.start()
	server_display2=ServerDisplay("ip_here")
	server_display2.start()
	server_display2=ServerDisplay("ip_here")
	server_display2.start()
	cpu_data1=[]
	memory_data1=[]
	disk_data1=[]
	timestamps1=[]

	cpu_data2=[]
	memory_data2=[]
	disk_data2=[]
	timestamps2=[]
	with tab1:
		error_placeholder=st.empty()
		cpu_placeholder1 = st.empty()
		memory_placeholder1 = st.empty()
		disk_placeholder1 = st.empty()
		line_chart_placeholder1=st.empty()
		def update_tab1():
			if (server_display1.cpu,server_display1.memory,server_display1.disk)==(0,0,0):
				print('YUP')
				error_placeholder.subheader("No connection")
				return
			timestamp = time.strftime('%H:%M:%S')
			cpu_data1.append(server_display1.cpu)
			memory_data1.append(server_display1.memory)
			disk_data1.append(server_display1.disk)
			timestamps1.append(timestamp)
			data = {
                "Timestamp": timestamps1,
                "CPU (%)": cpu_data1,
                "Memory (%)": memory_data1,
                "Disk (%)": disk_data1,
            }
			stats_df = pd.DataFrame(data)
			line_chart_placeholder1.line_chart(stats_df,x='Timestamp',y=['CPU (%)',"Memory (%)","Disk (%)"])
			cpu_placeholder1.metric("CPU Usage", f"{server_display1.cpu}%")
			memory_placeholder1.metric("Memory Usage", f"{server_display1.memory}%")
			disk_placeholder1.metric("Disk Usage", f"{server_display1.disk}%")
			
		
	with tab2:
		error_placeholder=st.empty()
		cpu_placeholder2 = st.empty()
		memory_placeholder2 = st.empty()
		disk_placeholder2 = st.empty()
		line_chart_placeholder2=st.empty()
		def update_tab2():
			if (server_display2.cpu,server_display2.memory,server_display2.disk)==(0,0,0):
				print('YUP')
				error_placeholder.subheader("No connection")
				return
			error_placeholder.empty()
			timestamp = time.strftime('%H:%M:%S')
			cpu_data2.append(server_display2.cpu)
			memory_data2.append(server_display2.memory)
			disk_data2.append(server_display2.disk)
			timestamps2.append(timestamp)
			data = {
                "Timestamp": timestamps2,
                "CPU (%)": cpu_data2,
                "Memory (%)": memory_data2,
                "Disk (%)": disk_data2,
            }
			stats_df = pd.DataFrame(data)
			line_chart_placeholder2.line_chart(stats_df,x='Timestamp',y=['CPU (%)',"Memory (%)","Disk (%)"])
			cpu_placeholder2.metric("CPU Usage", f"{server_display2.cpu}%")
			memory_placeholder2.metric("Memory Usage", f"{server_display2.memory}%")
			disk_placeholder2.metric("Disk Usage", f"{server_display2.disk}%")
	with tab3:
		#st.header("An owl")
		st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
	
	while True:
		#this is the logic loop that calls updates
		update_tab1()
		update_tab2()
		time.sleep(5)

if __name__ == '__main__':
	main()