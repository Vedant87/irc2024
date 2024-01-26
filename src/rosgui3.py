import subprocess
import rospy
import tkinter as tk
from std_msgs.msg import Int32, Int16MultiArray, String, Bool

class ROSNodeControlGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("ROS Control GUI")

        # ROS Node Status
        self.node_status_label1 = tk.Label(master, text="\n       CAM AND ACTUATORS       ", fg="#1434A4", font=('Roboto','20','bold'), bg="#ADD8E6")
        self.node_status_label1.grid(row=0,column=0)

        self.node_status_label2 = tk.Label(master, text="\n       BASE, BEVEL AND STEPPER       ", fg= "#1434A4", font=('Roboto','20','bold'), bg="#ADD8E6")
        self.node_status_label2.grid(row=0,column=1)

        self.step_indicator_label= tk.Label(master, text="\n       STEPPER STATE       \n", fg="#1434A4", font=('Roboto','12','bold'), bg="#ADD8E6")
        self.step_indicator_label.grid(row=2,column=2)

        self.master_status_label = tk.Label(master, text="ROSMASTER", fg="#1434A4", font=('Roboto','20','bold'), bg="#ADD8E6")
        self.master_status_label.grid(row=6,column=2)

        self.node_status_var1 = tk.StringVar()
        self.node_status_display1 = tk.Label(master, textvariable=self.node_status_var1, bg="#ADD8E6")
        self.node_status_display1.grid(row=1,column=0)

        self.node_status_var2 = tk.StringVar()
        self.node_status_display2 = tk.Label(master, textvariable=self.node_status_var2, bg="#ADD8E6")
        self.node_status_display2.grid(row=1,column=1)

        self.master_status_var = tk.StringVar()
        self.master_status_display = tk.Label(master, textvariable=self.master_status_var, bg="#ADD8E6")
        self.master_status_display.grid(row=7,column=2)

        # Start ROS Node Button
        self.start_button1 = tk.Button(master, text="Start ROS Node", command=self.start_ros_node1, bg="red", fg="white", font=('Helvetica', '16'))
        self.start_button1.grid(row=2,column=0)

        self.start_button2 = tk.Button(master, text="Start ROS Node", command=self.start_ros_node2, bg="red", fg="white", font=('Helvetica', '16'))
        self.start_button2.grid(row=2,column=1)

        self.start_master_button = tk.Button(master, text="Start ROS Master", command=self.start_ros_master, bg="red", fg="white", font=('Helvetica', '16'))
        self.start_master_button.grid(row=8,column=2)



        # Stop ROS Node Button
        self.stop_button1 = tk.Button(master, text="Stop ROS Node", command=self.stop_ros_node1, bg="yellow", fg="black", font=('Helvetica', '16'))
        self.stop_button1.grid(row=3,column=0)

        self.stop_button2 = tk.Button(master, text="Stop ROS Node", command=self.stop_ros_node2, bg="yellow", fg="black", font=('Helvetica', '16'))
        self.stop_button2.grid(row=3,column=1)

        self.stop_master_button = tk.Button(master, text="Stop ROS Master", command=self.stop_ros_master, bg="yellow", fg="black", font=('Helvetica', '16'))
        self.stop_master_button.grid(row=9,column=2)

        # Stepper Condition Indicator
        self.step_indicator = tk.Button(master, text="       ", state=tk.DISABLED)
        self.step_indicator.grid(row=3, column =2)

        # ROS Topic Messages
        self.message_label1 = tk.Label(master, text="\nROS Topic Messages:\n", font=('Helvetica', '14', 'bold'), bg="#ADD8E6")
        self.message_label1.grid(row=4,column=0)

        self.message_label2 = tk.Label(master, text="\nROS Topic Messages:\n", font=('Helvetica', '14', 'bold'), bg="#ADD8E6")
        self.message_label2.grid(row=4,column=1)

        self.message_var1 = tk.StringVar()
        self.message_display1 = tk.Label(master, textvariable=self.message_var1, font=('Helvetica', '12'), bg="#ADD8E6")
        self.message_display1.grid(row=5,column=0)

        self.message_var2 = tk.StringVar()
        self.message_display2 = tk.Label(master, textvariable=self.message_var2, font=('Helvetica', '12'), bg="#ADD8E6")
        self.message_display2.grid(row=5,column=1)

        # ROS Subscriber
        rospy.init_node('ros_gui_node', anonymous=True)
        self.subscriber1 = rospy.Subscriber("/control1", Int16MultiArray, self.callback1)
        self.subscriber2 = rospy.Subscriber("/control2", Int16MultiArray, self.callback2)
        

        # Variables to store subprocess and its PID
        self.ros_node_process1 = None
        self.ros_node_pid1 = None

        self.ros_node_process2 = None
        self.ros_node_pid2 = None

        self.ros_master_process = None

    def start_ros_node1(self):

        ros_node_command1 = 'rosrun my_package cam_la_v2.py'
        self.start_button1.config(state=tk.DISABLED)

        try:
            self.ros_node_process1 = subprocess.Popen(ros_node_command1, shell=True)
            self.ros_node_pid1 = self.ros_node_process1.pid
            self.node_status_var1.set(f"Node is Running (PID: {self.ros_node_pid1})")
        except Exception as e:
            self.node_status_var1.set(f"Error starting ROS node: {str(e)}")

    def start_ros_node2(self):

        ros_node_command2 = 'rosrun my_package base_bevel_v2.py'
        self.start_button2.config(state=tk.DISABLED)

        try:
            self.ros_node_process2 = subprocess.Popen(ros_node_command2, shell=True)
            self.ros_node_pid2 = self.ros_node_process2.pid
            self.node_status_var2.set(f"Node is Running (PID: {self.ros_node_pid2})")
        except Exception as e:
            self.node_status_var2.set(f"Error starting ROS node: {str(e)}")

    def start_ros_master(self):

        ros_command_master = 'roscore'
        self.start_master_button.config(state=tk.DISABLED)

        try:
            self.ros_master_process = subprocess.Popen(ros_command_master, shell=True)
            self.master_status_var.set(f"ROS Master is Running")
        except Exception as e:
            self.master_status_var.set(f"Error starting ROS node: {str(e)}")

    def stop_ros_node1(self):

        self.start_button1.config(state=tk.ACTIVE)

        if self.ros_node_process1:
            try:
                termination_publisher1.publish(Bool(True))
                self.node_status_var1.set("Node Stopped")
            except Exception as e:
                self.node_status_var1.set(f"Error stopping ROS node: {str(e)}")

    def stop_ros_node2(self):

        self.start_button2.config(state=tk.ACTIVE)

        if self.ros_node_process2:
            try:
                termination_publisher2.publish(Bool(True))
                self.node_status_var2.set("Node Stopped")
            except Exception as e:
                self.node_status_var2.set(f"Error stopping ROS node: {str(e)}")

    def stop_ros_master(self):

        self.start_master_button.config(state=tk.ACTIVE)
        stop_master_command = 'pkill -f rosmaster'

        if self.ros_master_process:
            try:
                self.stop_master = subprocess.Popen(stop_master_command, shell=True)
                self.master_status_var.set("ROS Master Stopped")
            except Exception as e:
                self.master_status_var.set(f"Error stopping ROS master: {str(e)}")

    def callback1(self, data):
        self.message_var1.set(data.data)
        self.enable_state = 3

        if data.data[2] == 1:
            self.enable_state = 1
        elif data.data[2] == 2:
            self.enable_state = 0

        if self.enable_state == 1:
            self.step_indicator.config(text="ENABLED", bg="green", fg="white")
        elif self.enable_state == 0:
            self.step_indicator.config(text="DISABLED", bg="red", fg="white")

    def callback2(self, data):
        self.message_var2.set(data.data)

if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="#ADD8E6")
    termination_publisher1 = rospy.Publisher('termination_signal1', Bool, queue_size=10)
    termination_publisher2 = rospy.Publisher('termination_signal2', Bool, queue_size=10)
    gui = ROSNodeControlGUI(root)
    root.geometry("2500x1000")
    root.mainloop()
