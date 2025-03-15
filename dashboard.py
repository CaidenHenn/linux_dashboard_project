import streamlit as st
import requests
import time
from threading import Thread
st.title("Linux Monitoring Dashboard")


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
		if response.status_code == 200:
			data = response.json()
			self.cpu = data["CPU"]
			self.memory = data["Memory"]
			self.disk = data["HDD (Disk)"]
			
		else:
			self.cpu = self.memory = self.disk = "Error"
		
	
def main():
	tab1, tab2, tab3 = st.tabs(["Server1", "Server2", "Server3"])
	#make threads to fetch api data from different servers
	server_display1=ServerDisplay("http://35.231.107.155:5000/stats")
	server_display1.start()
	with tab1:
		cpu_placeholder = st.empty()
		memory_placeholder = st.empty()
		disk_placeholder = st.empty()
		def update_tab1():
			cpu_placeholder.metric("CPU Usage", f"{server_display1.cpu}%")
			memory_placeholder.metric("Memory Usage", f"{server_display1.memory}%")
			disk_placeholder.metric("Disk Usage", f"{server_display1.disk}%")
			
		
	with tab2:
		st.header("A dog")
		st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
	with tab3:
		st.header("An owl")
		st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
	
	while True:
		#this is the logic loop that calls updates
		update_tab1()
		time.sleep(2)

if __name__ == '__main__':
	main()