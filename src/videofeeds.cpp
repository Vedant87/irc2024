#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
#include <sstream> // for converting the command line parameter to integer

int main(int argc, char** argv)
{
  // Check if video source has been passed as a parameter
  if(argv[1] == NULL) return 1;

  ros::init(argc, argv, "image_publisher",ros::init_options::AnonymousName);
  ros::NodeHandle nh;
  image_transport::ImageTransport it(nh);
  image_transport::Publisher pub = it.advertise("video_frame1/image", 1);

  // Convert the passed as command line parameter index for the video device to an integer
  std::istringstream video_sourceCmd(argv[1]);
  int video_source;
  // Check if it is indeed a number
  if(!(video_sourceCmd >> video_source)) return 1;

  cv::VideoCapture cap(video_source);
  cap.set(cv::CAP_PROP_FRAME_WIDTH,640);
  cap.set(cv::CAP_PROP_FRAME_HEIGHT,360);
  // Check if video device can be opened with the given index
  if(!cap.isOpened()) return 1;
  cv::Mat frame;
  sensor_msgs::ImagePtr msg1;

    // if(argv[2] == NULL) return 1;

//   ros::init(argc, argv, "image_publisher",ros::init_options::AnonymousName);
//   ros::NodeHandle nh;
//   image_transport::ImageTransport it(nh);
  image_transport::Publisher pub2 = it.advertise("video_frame2/image", 1);

  // Convert the passed as command line parameter index for the video device to an integer
  std::istringstream video_sourceCmd2(argv[2]);
  int video_source2;
  // Check if it is indeed a number
  if(!(video_sourceCmd2 >> video_source2)) return 1;

  cv::VideoCapture cap2(video_source2);
  cap2.set(cv::CAP_PROP_FRAME_WIDTH,640);
  cap2.set(cv::CAP_PROP_FRAME_HEIGHT,360);
  // Check if video device can be opened with the given index
  if(!cap2.isOpened()) return 1;
  cv::Mat frame2;
  sensor_msgs::ImagePtr msg2;

  ros::Rate loop_rate(30);




  while (nh.ok()) {
    cap >> frame;
    // Check if grabbed frame is actually full with some content
    if(!frame.empty()) {
      msg1 = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();
      pub.publish(msg1);
    //  cv::waitKey(1);
    }
    if(!frame2.empty()) {
      msg2 = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();
      pub.publish(msg2);
    //  cv::waitKey(1);
    }
    ros::spinOnce();
    loop_rate.sleep();
  }
}