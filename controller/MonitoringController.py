# -*- coding: utf-8 -*-
import AbstractController
class MonitoringController(AbstractController):
  def  __init__(self, writer_controller,time_source_controller):
        self.writer_controller=writer_controller
        self.time_source_controller=time_source_controller
        
        
  def new_monitoring_record(self,record):
        return self.writer_controller.new_monitoring_record(record)      