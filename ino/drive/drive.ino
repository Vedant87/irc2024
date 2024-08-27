#include <ArduinoHardware.h>
#include <geometry_msgs/Point.h>

#include <Cytron_SmartDriveDuo.h>
#include <ros.h>

ros::NodeHandle nh;

#define IN1 17
#define IN2 16
#define IN3 21
#define BAUDRATE 115200
Cytron_SmartDriveDuo motor_back(SERIAL_SIMPLIFIED, IN1, BAUDRATE);
Cytron_SmartDriveDuo motor_mid(SERIAL_SIMPLIFIED, IN2, BAUDRATE);
Cytron_SmartDriveDuo motor_front(SERIAL_SIMPLIFIED, IN3, BAUDRATE);

geometry_msgs::Point vels;

ros::Publisher pub1("feedback", &vels);

 float right_wheel_mid=0; 
 float left_wheel_mid=0;
  float right_wheel_front=0; 
 float left_wheel_front=0;
  float right_wheel_back=0; 
 float left_wheel_back=0;
 float velx,velz=0;
 


void callback(const geometry_msgs::Point& msg)
{ 
  velx=msg.x*0.67;
  velz=msg.z*0.67;
 angular=abs((velx-velz))
 
  if(angular<5){
   right_wheel_mid = velx;
  left_wheel_mid = velz;
  right_wheel_front = velx;
  left_wheel_mid_front = velz;
  right_wheel_back = velx;
  left_wheel_back = velz;
  }
else{
  right_wheel_mid = velx;
  left_wheel_mid = velz;
  right_wheel_front = velx*1.488;
  left_wheel_mid_front = velz*1.488;
  right_wheel_back = velx*1.33;
  left_wheel_back = velz*1.33;
  vels.x = right_wheel;
  vels.y = left_wheel;
  
}
pub1.publish(&vels);

ros::Subscriber<geometry_msgs::Point> sub("/rover",&callback);

void setup()
{ 
  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(pub1);
}

void loop()
{
  motor_back.control(left_wheel_back,right_wheel_back);
  motor_mid.control(left_wheel_mid,right_wheel_mid);
  motor_front.control(left_wheel_front,right_wheel_front);
  nh.spinOnce();
}
