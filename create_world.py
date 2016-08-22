import random

colors = ["Blue", "Green", "Red"]
random.shuffle(colors)
color1 = colors[0]
color2 = colors[1]
color3 = colors[2]
print color3 + " " + color2 + " " + color1
str = """
<sdf version='1.4'>
  <world name='default'>
    <light name='sun' type='directional'>
      <cast_shadows>1</cast_shadows>
      <pose>0 0 10 0 -0 0</pose>
      <diffuse>0.8 0.8 0.8 1</diffuse>
      <specular>0.2 0.2 0.2 1</specular>
      <attenuation>
        <range>1000</range>
        <constant>0.9</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <direction>-0.5 0.1 -0.9</direction>
    </light>
    <model name='ground_plane'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>100</mu>
                <mu2>50</mu2>
              </ode>
            </friction>
            <bounce/>
            <contact>
              <ode/>
            </contact>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='visual'>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
          </material>
        </visual>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
    </model>
    <physics type='ode'>
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1</real_time_factor>
      <real_time_update_rate>1000</real_time_update_rate>
      <gravity>0 0 -9.8</gravity>
    </physics>
    <scene>
      <ambient>0.4 0.4 0.4 1</ambient>
      <background>0.7 0.7 0.7 1</background>
      <shadows>1</shadows>
    </scene>
    <spherical_coordinates>
      <surface_model>EARTH_WGS84</surface_model>
      <latitude_deg>0</latitude_deg>
      <longitude_deg>0</longitude_deg>
      <elevation>0</elevation>
      <heading_deg>0</heading_deg>
    </spherical_coordinates>
    <model name='komodo_1'>
      <link name='dummy_link'>
        <pose>0 0 0 0 -0 0</pose>
        <inertial>
          <pose>-0.00746355 0.000195313 0.244582 0 -0 0</pose>
          <mass>13.9073</mass>
          <inertia>
            <ixx>1.04639</ixx>
            <ixy>-0.00111871</ixy>
            <ixz>0.0457727</ixz>
            <iyy>1.21254</iyy>
            <iyz>0.000147165</iyz>
            <izz>0.378865</izz>
          </inertia>
        </inertial>
        <collision name='dummy_link_collision_Arm_base_link'>
          <pose>-0.11225 0 0.167161 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Arm_base_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode/>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <collision name='dummy_link_collision_Asus_Camera_link'>
          <pose>0.031208 0 0.863395 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Asus_Camera_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode/>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <collision name='dummy_link_collision_Front_Camera_link'>
          <pose>0.26225 0.0875 0.1 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Front_Camera_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode/>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <collision name='dummy_link_collision_Laser_link'>
          <pose>0.234263 0 0.145827 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Laser_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode/>
            </friction>
            <bounce/>
          </surface>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode/>
            </friction>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <collision name='dummy_link_collision_Left_URF_link'>
          <pose>-0.0223641 0.13725 0.138508 -9.97271e-33 -1.52736e-16 1.5708</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Left_URF_link.STL</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>
        <collision name='dummy_link_collision_Rear_Camera_link'>
          <pose>-0.079292 0 0.521661 0 -0 3.13319</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Rear_Camera_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode/>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <collision name='dummy_link_collision_Rear_URF_link'>
          <pose>-0.2675 -5.08e-05 0.108 -2.22045e-16 1.676e-38 3.14159</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Rear_URF_link.STL</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>
        <collision name='dummy_link_collision_Right_URF_link'>
          <pose>-0.0222625 -0.13725 0.138508 -7.39076e-33 2.91353e-16 -1.5708</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Right_URF_link.STL</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>
        <collision name='dummy_link_collision_Top_Camera_link'>
          <pose>-0.050042 0.015283 0.827161 0 -1.57 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Top_Camera_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode/>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <collision name='dummy_link_collision_base_link'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/base_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
              </ode>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <collision name='dummy_link_collision_sensors_unit_link'>
          <pose>-0.00199997 0 0.0835 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/sensors_unit_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode/>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='dummy_link_visual_Arm_base_link'>
          <pose>-0.11225 0 0.167161 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Arm_base_link.STL</uri>
            </mesh>
          </geometry>
          <material>
            <script>
              <name>Gazebo/White</name>
              <uri>__default__</uri>
            </script>
          </material>
          <material>
            <script>
              <name>Gazebo/White</name>
              <uri>__default__</uri>
            </script>
          </material>
        </visual>
        <visual name='dummy_link_visual_Asus_Camera_link'>
          <pose>0.031208 0 0.863395 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Asus_Camera_link.STL</uri>
            </mesh>
          </geometry>
        </visual>
        <visual name='dummy_link_visual_Front_Camera_link'>
          <pose>0.26225 0.0875 0.1 -1.5708 2.74384e-16 -1.5708</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Front_Camera_link.STL</uri>
            </mesh>
          </geometry>
        </visual>
        <visual name='dummy_link_visual_Laser_link'>
          <pose>0.234263 0 0.145827 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Laser_link.STL</uri>
            </mesh>
          </geometry>
          <material>
            <script>
              <name>Gazebo/Grey</name>
              <uri>__default__</uri>
            </script>
          </material>
        </visual>
        <visual name='dummy_link_visual_Left_URF_link'>
          <pose>-0.0223641 0.13725 0.138508 -9.97271e-33 -1.52736e-16 1.5708</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Left_URF_link.STL</uri>
            </mesh>
          </geometry>
        </visual>
        <visual name='dummy_link_visual_Rear_Camera_link'>
          <pose>-0.079292 0 0.521661 1.57 1.17067e-16 -1.58</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Rear_Camera_link.STL</uri>
            </mesh>
          </geometry>
        </visual>
        <visual name='dummy_link_visual_Rear_URF_link'>
          <pose>-0.2675 -5.08e-05 0.108 -2.22045e-16 1.676e-38 3.14159</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Rear_URF_link.STL</uri>
            </mesh>
          </geometry>
        </visual>
        <visual name='dummy_link_visual_Right_URF_link'>
          <pose>-0.0222625 -0.13725 0.138508 -7.39076e-33 2.91353e-16 -1.5708</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Right_URF_link.STL</uri>
            </mesh>
          </geometry>
        </visual>
        <visual name='dummy_link_visual_Top_Camera_link'>
          <pose>-0.050042 0.015283 0.827161 1.57 -0.00345758 -1.57079</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Top_Camera_link.STL</uri>
            </mesh>
          </geometry>
        </visual>
        <visual name='dummy_link_visual_base_link'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/base_link.STL</uri>
            </mesh>
          </geometry>
          <material>
            <script>
              <name>Gazebo/White</name>
              <uri>__default__</uri>
            </script>
          </material>
        </visual>
        <visual name='dummy_link_visual_sensors_unit_link'>
          <pose>-0.00199997 0 0.0835 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/sensors_unit_link.STL</uri>
            </mesh>
          </geometry>
          <material>
            <script>
              <name>Gazebo/White</name>
              <uri>__default__</uri>
            </script>
          </material>
        </visual>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <sensor name='Asus_Camera_link' type='depth'>
          <visualize>1</visualize>
          <update_rate>20</update_rate>
          <camera name='__default__'>
            <horizontal_fov>2</horizontal_fov>
            <image>
              <format>R8G8B8</format>
              <width>640</width>
              <height>480</height>
            </image>
            <clip>
              <near>0.5</near>
              <far>9</far>
            </clip>
          </camera>
          <plugin name='Asus_Camera_link_camera_controller' filename='libgazebo_ros_openni_kinect.so'>
            <alwaysOn>true</alwaysOn>
            <updateRate>20</updateRate>
            <cameraName>Asus_Camera</cameraName>
            <imageTopicName>rgb/image_raw</imageTopicName>
            <cameraInfoTopicName>rgb/camera_info</cameraInfoTopicName>
            <depthImageTopicName>depth/image_raw</depthImageTopicName>
            <depthImageCameraInfoTopicName>depth/camera_info</depthImageCameraInfoTopicName>
            <pointCloudTopicName>depth/rotated_points</pointCloudTopicName>
            <pointCloudCutoff>0.4</pointCloudCutoff>
            <pointCloudCutoffMax>50.0</pointCloudCutoffMax>
            <frameName>/Asus_Camera_link</frameName>
            <distortion_k1>0.0</distortion_k1>
            <distortion_k2>0.0</distortion_k2>
            <distortion_k3>0.0</distortion_k3>
            <distortion_t1>0.0</distortion_t1>
            <distortion_t2>0.0</distortion_t2>
            <robotNamespace>/komodo_1/</robotNamespace>
          </plugin>
          <pose>0.031208 0 0.863395 0 -0 0</pose>
        </sensor>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <sensor name='camera1' type='camera'>
          <visualize>0</visualize>
          <update_rate>30</update_rate>
          <camera name='rear_camera'>
            <horizontal_fov>2</horizontal_fov>
            <image>
              <width>1800</width>
              <height>1800</height>
              <format>R8G8B8</format>
            </image>
            <clip>
              <near>0.02</near>
              <far>9</far>
            </clip>
          </camera>
          <plugin name='libgazebo' filename='libgazebo_ros_camera.so'>
            <alwaysOn>true</alwaysOn>
            <robotNamespace>komodo_1</robotNamespace>
            <cameraName>rear_camera</cameraName>
            <imageTopicName>image_raw</imageTopicName>
            <cameraInfoTopicName>camera_info</cameraInfoTopicName>
            <frameName>Rear_Camera_link</frameName>
            <hackBaseline>0.07</hackBaseline>
            <distortionK1>0.0</distortionK1>
            <distortionK2>0.0</distortionK2>
            <distortionK3>0.0</distortionK3>
            <distortionT1>0.0</distortionT1>
            <distortionT2>0.0</distortionT2>
          </plugin>
          <pose>-0.079292 0 0.521661 0 -0 3.13319</pose>
        </sensor>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <sensor name='camera1' type='camera'>
          <visualize>0</visualize>
          <update_rate>30</update_rate>
          <camera name='rear_camera'>
            <horizontal_fov>2</horizontal_fov>
            <image>
              <width>1800</width>
              <height>1800</height>
              <format>R8G8B8</format>
            </image>
            <clip>
              <near>0.02</near>
              <far>9</far>
            </clip>
          </camera>
          <plugin name='libgazebo' filename='libgazebo_ros_camera.so'>
            <alwaysOn>true</alwaysOn>
            <robotNamespace>komodo_1</robotNamespace>
            <cameraName>top_camera</cameraName>
            <imageTopicName>image_raw</imageTopicName>
            <cameraInfoTopicName>camera_info</cameraInfoTopicName>
            <frameName>Top_Camera_link</frameName>
            <hackBaseline>0.07</hackBaseline>
            <distortionK1>0.0</distortionK1>
            <distortionK2>0.0</distortionK2>
            <distortionK3>0.0</distortionK3>
            <distortionT1>0.0</distortionT1>
            <distortionT2>0.0</distortionT2>
          </plugin>
          <pose>-0.050042 0.015283 0.827161 0 -1.57 0</pose>
        </sensor>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <sensor name='camera2' type='camera'>
          <visualize>0</visualize>
          <update_rate>30</update_rate>
          <camera name='Front_Camera'>
            <horizontal_fov>2</horizontal_fov>
            <image>
              <width>1800</width>
              <height>1800</height>
              <format>R8G8B8</format>
            </image>
            <clip>
              <near>0.02</near>
              <far>9</far>
            </clip>
          </camera>
          <plugin name='camera_controller' filename='libgazebo_ros_camera.so'>
            <alwaysOn>true</alwaysOn>
            <robotNamespace>komodo_1</robotNamespace>
            <cameraName>Front_Camera</cameraName>
            <imageTopicName>image_raw</imageTopicName>
            <cameraInfoTopicName>camera_info</cameraInfoTopicName>
            <frameName>Front_Camera_link</frameName>
            <hackBaseline>0.07</hackBaseline>
            <distortionK1>0.0</distortionK1>
            <distortionK2>0.0</distortionK2>
            <distortionK3>0.0</distortionK3>
            <distortionT1>0.0</distortionT1>
            <distortionT2>0.0</distortionT2>
          </plugin>
          <pose>0.26225 0.0875 0.1 0 -0 0</pose>
        </sensor>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <sensor name='head_hokuyo_sensor' type='ray'>
          <visualize>0</visualize>
          <update_rate>10</update_rate>
          <ray>
            <scan>
              <horizontal>
                <samples>720</samples>
                <resolution>1</resolution>
                <min_angle>-1.5708</min_angle>
                <max_angle>1.5708</max_angle>
              </horizontal>
            </scan>
            <range>
              <min>0.1</min>
              <max>30</max>
              <resolution>0.01</resolution>
            </range>
            <noise>
              <type>gaussian</type>
              <mean>0</mean>
              <stddev>0.01</stddev>
            </noise>
          </ray>
          <plugin name='gazebo_ros_head_hokuyo_controller' filename='libgazebo_ros_laser.so'>
            <topicName>scan</topicName>
            <frameName>Laser_link</frameName>
            <robotNamespace>/komodo_1/</robotNamespace>
          </plugin>
          <pose>0.234263 0 0.145827 0 -0 0</pose>
        </sensor>
        <gravity>1</gravity>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <link name='elevator_link'>
        <pose>-0.010792 0 0.241161 0 -0 0</pose>
        <inertial>
          <pose>0.0954672 1.91586e-06 -0.0185743 0 -0 0</pose>
          <mass>1.09058</mass>
          <inertia>
            <ixx>0.000835857</ixx>
            <ixy>5.81871e-08</ixy>
            <ixz>-3.13494e-05</ixz>
            <iyy>0.00128841</iyy>
            <iyz>1.45397e-07</iyz>
            <izz>0.00136461</izz>
          </inertia>
        </inertial>
        <collision name='elevator_link_collision'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/elevator_link.STL</uri>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>
        <visual name='elevator_link_visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/elevator_link.STL</uri>
            </mesh>
          </geometry>
        </visual>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <joint name='elevator_joint' type='prismatic'>
        <child>elevator_link</child>
        <parent>dummy_link</parent>
        <axis>
          <xyz>0 0 1</xyz>
          <limit>
            <lower>0</lower>
            <upper>0.5</upper>
            <effort>100</effort>
            <velocity>1e-15</velocity>
          </limit>
          <dynamics>
            <damping>1000</damping>
          </dynamics>
        </axis>
        <physics>
          <ode>
            <fudge_factor>100.99</fudge_factor>
            <limit>
              <cfm>0</cfm>
              <erp>0.2</erp>
            </limit>
          </ode>
        </physics>
      </joint>
      <link name='base_rotation_link'>
        <pose>0.102208 0 0.237161 -5.4637e-16 1.34659e-15 -2.1923e-31</pose>
        <inertial>
          <pose>-6.93889e-17 1.46538e-17 0.0623332 0 -0 0</pose>
          <mass>0.474</mass>
          <inertia>
            <ixx>0.00159426</ixx>
            <ixy>-8.40269e-08</ixy>
            <ixz>-1.60926e-19</ixz>
            <iyy>0.000605522</iyy>
            <iyz>-6.08768e-19</iyz>
            <izz>0.00123388</izz>
          </inertia>
        </inertial>
        <collision name='base_rotation_link_collision'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/base_rotation_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
              </ode>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='base_rotation_link_visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/base_rotation_link.STL</uri>
            </mesh>
          </geometry>
          <material>
            <script>
              <name>Gazebo/Grey</name>
              <uri>__default__</uri>
            </script>
          </material>
        </visual>
        <gravity>1</gravity>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <joint name='base_rotation_joint' type='revolute'>
        <child>base_rotation_link</child>
        <parent>elevator_link</parent>
        <axis>
          <xyz>0 0 1</xyz>
          <limit>
            <lower>-1.57079</lower>
            <upper>1.57079</upper>
            <effort>10</effort>
            <velocity>0</velocity>
          </limit>
          <dynamics/>
        </axis>
      </joint>
      <link name='shoulder_link'>
        <pose>0.102208 4.56219e-17 0.320661 -5.4637e-16 1.34659e-15 -2.1923e-31</pose>
        <inertial>
          <pose>-4.66248e-06 -9.82289e-05 0.0772888 0 -0 0</pose>
          <mass>0.191481</mass>
          <inertia>
            <ixx>0.00107302</ixx>
            <ixy>-2.97891e-07</ixy>
            <ixz>-2.01215e-08</ixz>
            <iyy>0.000975953</iyy>
            <iyz>-1.19602e-06</iyz>
            <izz>0.00021766</izz>
          </inertia>
        </inertial>
        <collision name='shoulder_link_collision'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/shoulder_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
              </ode>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='shoulder_link_visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/shoulder_link.STL</uri>
            </mesh>
          </geometry>
          <material>
            <script>
              <name>Gazebo/Grey</name>
              <uri>__default__</uri>
            </script>
          </material>
        </visual>
        <gravity>1</gravity>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <joint name='shoulder_joint' type='revolute'>
        <child>shoulder_link</child>
        <parent>base_rotation_link</parent>
        <axis>
          <xyz>0 1 0</xyz>
          <limit>
            <lower>0</lower>
            <upper>1.69297</upper>
            <effort>10</effort>
            <velocity>0</velocity>
          </limit>
          <dynamics/>
        </axis>
      </joint>
      <link name='elbow1_link'>
        <pose>0.102208 -0.000251156 0.586966 -5.4637e-16 1.34659e-15 -2.1923e-31</pose>
        <inertial>
          <pose>3.38829e-05 2.66621e-06 0.0239321 0 -0 0</pose>
          <mass>0.235</mass>
          <inertia>
            <ixx>0.00111563</ixx>
            <ixy>3.16191e-07</ixy>
            <ixz>2.89268e-06</ixz>
            <iyy>0.00114606</iyy>
            <iyz>-8.11917e-08</iyz>
            <izz>0.000237163</izz>
          </inertia>
        </inertial>
        <collision name='elbow1_link_collision'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/elbow1_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
              </ode>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='elbow1_link_visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/elbow1_link.STL</uri>
            </mesh>
          </geometry>
          <material>
            <script>
              <name>Gazebo/Grey</name>
              <uri>__default__</uri>
            </script>
          </material>
        </visual>
        <gravity>1</gravity>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <joint name='elbow1_joint' type='revolute'>
        <child>elbow1_link</child>
        <parent>shoulder_link</parent>
        <axis>
          <xyz>-1 0 0</xyz>
          <limit>
            <lower>-2.4434</lower>
            <upper>2.4434</upper>
            <effort>10</effort>
            <velocity>0</velocity>
          </limit>
          <dynamics/>
        </axis>
      </joint>
      <link name='elbow2_link'>
        <pose>0.102208 -0.000251156 0.810966 -5.4637e-16 1.34659e-15 -2.1923e-31</pose>
        <inertial>
          <pose>0.000512285 -2.29085e-05 0.0885119 0 -0 0</pose>
          <mass>0.25</mass>
          <inertia>
            <ixx>0.0110437</ixx>
            <ixy>-3.04259e-07</ixy>
            <ixz>7.91667e-05</ixz>
            <iyy>0.0110599</iyy>
            <iyz>-1.22468e-06</iyz>
            <izz>0.000331598</izz>
          </inertia>
        </inertial>
        <collision name='elbow2_link_collision'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/elbow2_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
              </ode>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='elbow2_link_visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/elbow2_link.STL</uri>
            </mesh>
          </geometry>
          <material>
            <script>
              <name>Gazebo/Grey</name>
              <uri>__default__</uri>
            </script>
          </material>
        </visual>
        <gravity>1</gravity>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <joint name='elbow2_joint' type='revolute'>
        <child>elbow2_link</child>
        <parent>elbow1_link</parent>
        <axis>
          <xyz>0 1 0</xyz>
          <limit>
            <lower>-2.4434</lower>
            <upper>2.4434</upper>
            <effort>10</effort>
            <velocity>0</velocity>
          </limit>
          <dynamics/>
        </axis>
      </joint>
      <link name='wrist_link'>
        <pose>0.115308 -0.000251156 1.05572 3.14159 -1.57079 -3.14159</pose>
        <inertial>
          <pose>0.0290615 2.04148e-06 0.0166629 0 -0 0</pose>
          <mass>0.287741</mass>
          <inertia>
            <ixx>0.000699632</ixx>
            <ixy>8.84413e-09</ixy>
            <ixz>1.71731e-05</ixz>
            <iyy>0.000393143</iyy>
            <iyz>-2.07107e-08</iyz>
            <izz>0.000579339</izz>
          </inertia>
        </inertial>
        <collision name='wrist_link_collision'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/wrist_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
              </ode>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <collision name='wrist_link_collision_Creative_Camera_link'>
          <pose>0.026025 0 0.052 -1.41059e-37 1.58022e-69 -6.20247e-16</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Creative_Camera_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
              </ode>
            </friction>
            <bounce/>
          </surface>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode/>
            </friction>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='wrist_link_visual'>
          <pose>0 0 0 3.14159 1.57079 3.14159</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/wrist_link.STL</uri>
            </mesh>
          </geometry>
        </visual>
        <visual name='wrist_link_visual_Creative_Camera_link'>
          <pose>0.026025 0 0.052 -1.41059e-37 1.58022e-69 -6.20247e-16</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/Creative_Camera_link.STL</uri>
            </mesh>
          </geometry>
        </visual>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <gravity>1</gravity>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <self_collide>0</self_collide>
        <sensor name='Creative_Camera_link' type='depth'>
          <visualize>1</visualize>
          <update_rate>20</update_rate>
          <camera name='__default__'>
            <horizontal_fov>2</horizontal_fov>
            <image>
              <format>R8G8B8</format>
              <width>640</width>
              <height>480</height>
            </image>
            <clip>
              <near>0.5</near>
              <far>9</far>
            </clip>
          </camera>
          <plugin name='Creative_Camera_link_camera_controller' filename='libgazebo_ros_openni_kinect.so'>
            <alwaysOn>true</alwaysOn>
            <updateRate>20</updateRate>
            <cameraName>Creative_Camera</cameraName>
            <imageTopicName>rgb/image_raw</imageTopicName>
            <cameraInfoTopicName>rgb/camera_info</cameraInfoTopicName>
            <depthImageTopicName>depth/image_raw</depthImageTopicName>
            <depthImageCameraInfoTopicName>depth/camera_info</depthImageCameraInfoTopicName>
            <pointCloudTopicName>depth/rotated_points</pointCloudTopicName>
            <pointCloudCutoff>0.4</pointCloudCutoff>
            <pointCloudCutoffMax>50.0</pointCloudCutoffMax>
            <frameName>/Creative_Camera_link</frameName>
            <distortion_k1>0.0</distortion_k1>
            <distortion_k2>0.0</distortion_k2>
            <distortion_k3>0.0</distortion_k3>
            <distortion_t1>0.0</distortion_t1>
            <distortion_t2>0.0</distortion_t2>
            <robotNamespace>/komodo_1/</robotNamespace>
          </plugin>
          <pose>0.026025 0 0.052 -1.41059e-37 1.58022e-69 -6.20247e-16</pose>
        </sensor>
        <kinematic>0</kinematic>
      </link>
      <joint name='wrist_joint' type='revolute'>
        <child>wrist_link</child>
        <parent>elbow2_link</parent>
        <axis>
          <xyz>1e-06 0 1</xyz>
          <limit>
            <lower>-1.91986</lower>
            <upper>1.91986</upper>
            <effort>10</effort>
            <velocity>0</velocity>
          </limit>
          <dynamics/>
        </axis>
      </joint>
      <link name='left_finger_link'>
        <pose>0.115308 0.0207488 1.09797 -5.46374e-16 1.29221e-15 -1.78545e-25</pose>
        <inertial>
          <pose>3.72404e-08 0.0148726 0.0333609 0 -0 0</pose>
          <mass>0.0045</mass>
          <inertia>
            <ixx>9.7735e-06</ixx>
            <ixy>8.75184e-13</ixy>
            <ixz>7.1723e-12</ixz>
            <iyy>1.16654e-05</iyy>
            <iyz>7.84012e-07</iyz>
            <izz>3.34837e-06</izz>
          </inertia>
        </inertial>
        <collision name='left_finger_link_collision'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/left_finger_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
              </ode>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='left_finger_link_visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/left_finger_link.STL</uri>
            </mesh>
          </geometry>
        </visual>
        <gravity>1</gravity>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <joint name='left_finger_joint' type='revolute'>
        <child>left_finger_link</child>
        <parent>wrist_link</parent>
        <axis>
          <xyz>1 0 0</xyz>
          <limit>
            <lower>-0.87266</lower>
            <upper>0.87266</upper>
            <effort>10</effort>
            <velocity>0</velocity>
          </limit>
          <dynamics/>
        </axis>
      </joint>
      <link name='right_finger_link'>
        <pose>0.115308 -0.0212512 1.09797 -5.46374e-16 1.29221e-15 -1.78545e-25</pose>
        <inertial>
          <pose>3.72404e-08 -0.0148726 0.0333609 0 -0 0</pose>
          <mass>0.0045</mass>
          <inertia>
            <ixx>9.7735e-06</ixx>
            <ixy>-8.75184e-13</ixy>
            <ixz>7.1723e-12</ixz>
            <iyy>1.16654e-05</iyy>
            <iyz>-7.84012e-07</iyz>
            <izz>3.34837e-06</izz>
          </inertia>
        </inertial>
        <collision name='right_finger_link_collision'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/right_finger_link.STL</uri>
            </mesh>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
              </ode>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='right_finger_link_visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/right_finger_link.STL</uri>
            </mesh>
          </geometry>
        </visual>
        <gravity>1</gravity>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <joint name='right_finger_joint' type='revolute'>
        <child>right_finger_link</child>
        <parent>wrist_link</parent>
        <axis>
          <xyz>1 0 0</xyz>
          <limit>
            <lower>-0.87266</lower>
            <upper>0.87266</upper>
            <effort>10</effort>
            <velocity>0</velocity>
          </limit>
          <dynamics/>
        </axis>
      </joint>
      <link name='FL_Wheel_link'>
        <pose>0.174 0.2009 0 -9.97271e-33 -1.52736e-16 1.5708</pose>
        <inertial>
          <pose>-0.00125662 1.4995e-05 2.59231e-06 0 -0 0</pose>
          <mass>3.83428</mass>
          <inertia>
            <ixx>0.0296526</ixx>
            <ixy>2.35765e-06</ixy>
            <ixz>-1.51001e-06</ixz>
            <iyy>0.0163721</iyy>
            <iyz>-1.22544e-06</iyz>
            <izz>0.016375</izz>
          </inertia>
        </inertial>
        <collision name='FL_Wheel_link_collision'>
          <pose>0 0 0 0 1.5 0</pose>
          <geometry>
            <cylinder>
              <length>0.05</length>
              <radius>0.1</radius>
            </cylinder>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
              </ode>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='FL_Wheel_link_visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/FL_Wheel_link.STL</uri>
            </mesh>
          </geometry>
          <material>
            <script>
              <name>Gazebo/Grey</name>
              <uri>__default__</uri>
            </script>
          </material>
        </visual>
        <gravity>1</gravity>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <joint name='FL_Wheel_joint' type='revolute'>
        <child>FL_Wheel_link</child>
        <parent>dummy_link</parent>
        <axis>
          <xyz>0 1 0</xyz>
          <limit>
            <lower>-1e+16</lower>
            <upper>1e+16</upper>
          </limit>
          <dynamics/>
        </axis>
      </joint>
      <link name='FR_Wheel_link'>
        <pose>0.174 -0.2009 0 -7.39076e-33 2.91353e-16 -1.5708</pose>
        <inertial>
          <pose>-0.00125662 1.11356e-05 1.03717e-05 0 -0 0</pose>
          <mass>3.83427</mass>
          <inertia>
            <ixx>0.0296525</ixx>
            <ixy>2.79965e-06</ixy>
            <ixz>2.53737e-08</ixz>
            <iyy>0.0163718</iyy>
            <iyz>8.36492e-07</iyz>
            <izz>0.0163752</izz>
          </inertia>
        </inertial>
        <collision name='FR_Wheel_link_collision'>
          <pose>0 0 0 0 1.5 0</pose>
          <geometry>
            <cylinder>
              <length>0.05</length>
              <radius>0.1</radius>
            </cylinder>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
              </ode>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='FR_Wheel_link_visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/FR_Wheel_link.STL</uri>
            </mesh>
          </geometry>
          <material>
            <script>
              <name>Gazebo/Grey</name>
              <uri>__default__</uri>
            </script>
          </material>
        </visual>
        <gravity>1</gravity>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <joint name='FR_Wheel_joint' type='revolute'>
        <child>FR_Wheel_link</child>
        <parent>dummy_link</parent>
        <axis>
          <xyz>0 1 0</xyz>
          <limit>
            <lower>-1e+16</lower>
            <upper>1e+16</upper>
          </limit>
          <dynamics/>
        </axis>
      </joint>
      <link name='RL_Wheel_link'>
        <pose>-0.156 0.2009 0 -9.97271e-33 -1.52736e-16 1.5708</pose>
        <inertial>
          <pose>-0.00125662 1.51826e-05 -1.03149e-06 0 -0 0</pose>
          <mass>3.83428</mass>
          <inertia>
            <ixx>0.0296526</ixx>
            <ixy>1.93315e-06</ixy>
            <ixz>-2.02526e-06</ixz>
            <iyy>0.0163728</iyy>
            <iyz>-1.75559e-06</iyz>
            <izz>0.0163742</izz>
          </inertia>
        </inertial>
        <collision name='RL_Wheel_link_collision'>
          <pose>0 0 0 0 1.5 0</pose>
          <geometry>
            <cylinder>
              <length>0.05</length>
              <radius>0.1</radius>
            </cylinder>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
              </ode>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='RL_Wheel_link_visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/RL_Wheel_link.STL</uri>
            </mesh>
          </geometry>
          <material>
            <script>
              <name>Gazebo/Grey</name>
              <uri>__default__</uri>
            </script>
          </material>
        </visual>
        <gravity>1</gravity>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <joint name='RL_Wheel_joint' type='revolute'>
        <child>RL_Wheel_link</child>
        <parent>dummy_link</parent>
        <axis>
          <xyz>0 1 0</xyz>
          <limit>
            <lower>-1e+16</lower>
            <upper>1e+16</upper>
          </limit>
          <dynamics/>
        </axis>
      </joint>
      <link name='RR_Wheel_link'>
        <pose>-0.156 -0.2009 0 -7.39076e-33 2.91353e-16 -1.5708</pose>
        <inertial>
          <pose>-0.00125662 1.11356e-05 1.03716e-05 0 -0 0</pose>
          <mass>3.83427</mass>
          <inertia>
            <ixx>0.0296525</ixx>
            <ixy>2.79965e-06</ixy>
            <ixz>2.53706e-08</ixz>
            <iyy>0.0163718</iyy>
            <iyz>8.36482e-07</iyz>
            <izz>0.0163752</izz>
          </inertia>
        </inertial>
        <collision name='RR_Wheel_link_collision'>
          <pose>0 0 0 0 1.5 0</pose>
          <geometry>
            <cylinder>
              <length>0.05</length>
              <radius>0.1</radius>
            </cylinder>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
              </ode>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='RR_Wheel_link_visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <mesh>
              <scale>1 1 1</scale>
              <uri>/home/liat/catkin_ws/src/ric_description/komodo/meshes_elevator/RR_Wheel_link.STL</uri>
            </mesh>
          </geometry>
          <material>
            <script>
              <name>Gazebo/Grey</name>
              <uri>__default__</uri>
            </script>
          </material>
        </visual>
        <gravity>1</gravity>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
      </link>
      <joint name='RR_Wheel_joint' type='revolute'>
        <child>RR_Wheel_link</child>
        <parent>dummy_link</parent>
        <axis>
          <xyz>0 1 0</xyz>
          <limit>
            <lower>-1e+16</lower>
            <upper>1e+16</upper>
          </limit>
          <dynamics/>
        </axis>
      </joint>
      <plugin name='gazebo_ros_control' filename='libgazebo_ros_control.so'>
        <robotNamespace>komodo_1</robotNamespace>
      </plugin>
      <static>0</static>
      <plugin name='skid_steer_drive_controller' filename='libgazebo_ros_skid_steer_drive.so'>
        <always_on>1</always_on>
        <updateRate>50.0</updateRate>
        <robotNamespace>/komodo_1</robotNamespace>
        <broadcastTF>1</broadcastTF>
        <leftFrontJoint>FL_Wheel_joint</leftFrontJoint>
        <rightFrontJoint>FR_Wheel_joint</rightFrontJoint>
        <leftRearJoint>RL_Wheel_joint</leftRearJoint>
        <rightRearJoint>RR_Wheel_joint</rightRearJoint>
        <wheelSeparation>0.5</wheelSeparation>
        <wheelDiameter>0.2</wheelDiameter>
        <robotBaseFrame>dummy_link</robotBaseFrame>
        <odometryTopic>diff_driver/odometry</odometryTopic>
        <odometryFrame>odom_link</odometryFrame>
        <torque>20</torque>
        <commandTopic>diff_driver/command</commandTopic>
      </plugin>
      <pose>0 0 0.1 0 -0 0</pose>
    </model>
    <model name='w1'>
      <link name='Wall_0'>
        <collision name='Wall_0_Collision'>
          <geometry>
            <box>
              <size>1.34 0.2 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>
        <visual name='Wall_0_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>1.34 0.2 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
          </material>
        </visual>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <pose>-4.85 -1.02 0 0 -0 0</pose>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <static>1</static>
    </model>
    <model name='c1'>
      <link name='Wall_3'>
        <collision name='Wall_3_Collision'>
          <geometry>
            <box>
              <size>0.21 0.2 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>
        <visual name='Wall_3_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.21 0.2 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/""" + color1 + """</name>
            </script>
          </material>
        </visual>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <pose>-3.475 -1.32 0 0 -0 0</pose>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <static>1</static>
    </model>
    <model name='c2'>
      <link name='Wall_6'>
        <collision name='Wall_6_Collision'>
          <geometry>
            <box>
              <size>0.21 0.2 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>
        <visual name='Wall_6_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.21 0.2 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/""" + color1 + """</name>
            </script>
          </material>
        </visual>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <pose>-2.715 -1.54 0 0 -0 0</pose>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <static>1</static>
    </model>
    <model name='w2'>
      <link name='Wall_8'>
        <collision name='Wall_8_Collision'>
          <geometry>
            <box>
              <size>1.56 0.2 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>
        <visual name='Wall_8_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>1.56 0.2 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
          </material>
        </visual>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <pose>-1.68 -1.34 0 0 -0 0</pose>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <static>1</static>
    </model>
    <model name='c3'>
      <link name='Wall_10'>
        <collision name='Wall_10_Collision'>
          <geometry>
            <box>
              <size>0.21 0.2 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>
        <visual name='Wall_10_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.21 0.2 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/""" + color2 + """</name>
            </script>
          </material>
        </visual>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <pose>-2.495 -2.02 0 0 -0 0</pose>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <static>1</static>
    </model>
    <model name='c4'>
      <link name='Wall_12'>
        <collision name='Wall_12_Collision'>
          <geometry>
            <box>
              <size>0.21 0.2 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>
        <visual name='Wall_12_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.21 0.2 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/""" + color2 + """</name>
            </script>
          </material>
        </visual>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <pose>-2.155 -1.58 0 0 -0 0</pose>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <static>1</static>
    </model>
    <model name='w3'>
      <link name='Wall_20'>
        <collision name='Wall_20_Collision'>
          <geometry>
            <box>
              <size>1.649 0.2 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>
        <visual name='Wall_20_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>1.649 0.2 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
          </material>
        </visual>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <pose>-1.576 -1.53317 0 0 -0 0</pose>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <static>1</static>
    </model>
    <model name='c5'>
      <link name='Wall_22'>
        <collision name='Wall_22_Collision'>
          <geometry>
            <box>
              <size>0.21 0.2 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>
        <visual name='Wall_22_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.21 0.2 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/""" + color3 + """</name>
            </script>
          </material>
        </visual>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <pose>-1.847 -3.12017 0 0 -0 0</pose>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <static>1</static>
    </model>
    <model name='c6'>
      <link name='Wall_29'>
        <collision name='Wall_29_Collision'>
          <geometry>
            <box>
              <size>0.21 0.2 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>
        <visual name='Wall_29_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.21 0.2 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/"""  + color3 + """</name>
            </script>
          </material>
        </visual>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <pose>-3.595 -3.02817 0 0 -0 0</pose>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <static>1</static>
    </model>
    <model name='w4'>
      <link name='Wall_31'>
        <collision name='Wall_31_Collision'>
          <geometry>
            <box>
              <size>1.695 0.2 2.5</size>
            </box>
          </geometry>
          <pose>0 0 1.25 0 -0 0</pose>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>
        <visual name='Wall_31_Visual'>
          <pose>0 0 1.25 0 -0 0</pose>
          <geometry>
            <box>
              <size>1.695 0.2 2.5</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
          </material>
        </visual>
        <velocity_decay>
          <linear>0</linear>
          <angular>0</angular>
        </velocity_decay>
        <pose>-2.2545 -3.29267 0 0 -0 0</pose>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <gravity>1</gravity>
      </link>
      <static>1</static>
    </model>
    <state world_name='default'>
      <sim_time>340 611000000</sim_time>
      <real_time>101 22576194</real_time>
      <wall_time>1471349774 159086787</wall_time>
      <model name='c1'>
        <pose>-0.60047 0.29228 0 0 -0 0</pose>
        <link name='Wall_3'>
          <pose>-4.07547 -1.02772 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='c2'>
        <pose>0.58799 0.53494 0 0 -0 0</pose>
        <link name='Wall_6'>
          <pose>-2.12701 -1.00506 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='c3'>
        <pose>2.10738 1.05663 0 0 -0 0</pose>
        <link name='Wall_10'>
          <pose>-0.387625 -0.963373 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='c4'>
        <pose>3.7894 0.629224 0 0 -0 0</pose>
        <link name='Wall_12'>
          <pose>1.6344 -0.950776 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='c5'>
        <pose>5.28312 2.10033 0 0 -0 0</pose>
        <link name='Wall_22'>
          <pose>3.43612 -1.01984 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='c6'>
        <pose>8.91391 1.92718 0 0 -0 0</pose>
        <link name='Wall_29'>
          <pose>5.31891 -1.10099 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='ground_plane'>
        <pose>0 0 0 0 -0 0</pose>
        <link name='link'>
          <pose>0 0 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='komodo_1'>
        <pose>1.03396 3.37925 0.101517 -5e-06 9.37041e-26 0.005906</pose>
        <link name='FL_Wheel_link'>
          <pose>1.20677 3.58117 0.101516 0.000671 1.8e-05 1.57671</pose>
          <velocity>-0.000107 0.000539 -0.001848 -0.005145 4e-06 0.000313</velocity>
          <acceleration>-0.11788 1.04565 -3.68778 -0.079339 -0.000313 0.002158</acceleration>
          <wrench>-0.451986 4.00931 -14.14 0 -0 0</wrench>
        </link>
        <link name='FR_Wheel_link'>
          <pose>1.20914 3.17938 0.101518 0.000371 1.1e-05 -1.56489</pose>
          <velocity>-8e-06 0.000522 0.001557 -0.005254 -0.000117 0.00025</velocity>
          <acceleration>0.030983 1.0088 3.11649 -0.081407 -0.000668 0.001611</acceleration>
          <wrench>0.118796 3.86799 11.9495 0 -0 0</wrench>
        </link>
        <link name='RL_Wheel_link'>
          <pose>0.876777 3.57922 0.101516 0.000968 2e-05 1.57671</pose>
          <velocity>-0.000113 0.000454 -0.001849 -0.004687 1.5e-05 0.000254</velocity>
          <acceleration>-0.129823 0.915422 -3.69063 -0.072439 -0.000552 0.001646</acceleration>
          <wrench>-0.497779 3.50998 -14.1509 0 -0 0</wrench>
        </link>
        <link name='RR_Wheel_link'>
          <pose>0.87915 3.17743 0.101518 0.000395 1.5e-05 -1.56489</pose>
          <velocity>2e-06 0.000447 0.001577 -0.004541 -2.1e-05 0.000258</velocity>
          <acceleration>0.05125 0.896183 3.15639 -0.070816 -8.3e-05 0.001687</acceleration>
          <wrench>0.196506 3.43621 12.1025 0 -0 0</wrench>
        </link>
        <link name='base_rotation_link'>
          <pose>1.13617 3.37985 0.338676 -3.1e-05 -8.7e-05 0.069108</pose>
          <velocity>-5.7e-05 0.002229 -0.00021 -0.002319 0.007069 0.006091</velocity>
          <acceleration>0.643781 4.88349 -0.409901 -0.095236 0.396557 0.569441</acceleration>
          <wrench>0.305152 2.31478 -0.194293 0 -0 0</wrench>
        </link>
        <link name='dummy_link'>
          <pose>1.03396 3.37925 0.101517 -5e-06 9.37041e-26 0.005906</pose>
          <velocity>-6e-05 0.000345 -0.00015 -0.008395 -2e-05 0.000291</velocity>
          <acceleration>-0.059849 4.79011 -0.297471 -1.26548 -0.002622 -0.042879</acceleration>
          <wrench>-0.832343 66.6175 -4.13702 0 -0 0</wrench>
        </link>
        <link name='elbow1_link'>
          <pose>1.11117 3.74167 0.090779 -1.22878 -0.000232 0.069036</pose>
          <velocity>-0.005788 0.000488 0.001966 0.027779 0.019496 0.014422</velocity>
          <acceleration>-6.88 -2.03107 7.05476 -0.336169 1.23633 1.79344</acceleration>
          <wrench>-1.6168 -0.477301 1.65787 0 -0 0</wrench>
        </link>
        <link name='elbow2_link'>
          <pose>1.54666 3.59765 0.029101 -1.33134 0.246519 -0.716526</pose>
          <velocity>-0.001905 0.001142 -0.01989 0.030748 0.015485 -0.012173</velocity>
          <acceleration>0.1683 -1.88648 -28.0908 0.422645 1.56663 -2.08698</acceleration>
          <wrench>0.042075 -0.47162 -7.0227 0 -0 0</wrench>
        </link>
        <link name='elevator_link'>
          <pose>1.02317 3.37919 0.342673 -2.4e-05 -3.1e-05 0.005905</pose>
          <velocity>-2e-06 0.002306 0.000118 -0.002325 0.00306 -0.00106</velocity>
          <acceleration>-0.049085 4.3062 -0.346674 -0.00526 0.006737 -0.249825</acceleration>
          <wrench>-0.053531 4.69626 -0.378076 0 -0 0</wrench>
        </link>
        <link name='left_finger_link'>
          <pose>1.18189 4.06297 0.0311 -1.46621 0.862977 -0.493767</pose>
          <velocity>0.000335 -0.000751 0.010225 0.029371 0.021216 -0.030463</velocity>
          <acceleration>-43.8195 8.77981 92.5498 0.096473 -0.00482 -0.03489</acceleration>
          <wrench>-0.197188 0.039509 0.416474 0 -0 0</wrench>
        </link>
        <link name='right_finger_link'>
          <pose>1.15919 4.0351 0.023681 -1.50993 0.863934 -0.493779</pose>
          <velocity>0.001164 -0.000638 0.011881 0.040684 0.039655 -0.03347</velocity>
          <acceleration>-41.3452 4.41513 74.0181 0.151663 0.142987 -0.04357</acceleration>
          <wrench>-0.186053 0.019868 0.333081 0 -0 0</wrench>
        </link>
        <link name='shoulder_link'>
          <pose>1.13616 3.37986 0.422176 -4.6e-05 -0.000101 0.069108</pose>
          <velocity>0.000446 0.002419 -0.000283 -0.000652 0.008432 0.005176</velocity>
          <acceleration>1.7513 5.44285 -0.534371 -0.485889 -0.124558 -0.000562</acceleration>
          <wrench>0.33534 1.0422 -0.102322 0 -0 0</wrench>
        </link>
        <link name='wrist_link'>
          <pose>1.43693 3.98484 0.249037 -0.671768 -0.232098 0.794728</pose>
          <velocity>0.002736 -0.002527 -0.007677 0.028524 0.015326 -0.012399</velocity>
          <acceleration>-0.409208 -0.781361 -0.12855 -1.22703 -0.702297 -0.401347</acceleration>
          <wrench>-0.117746 -0.22483 -0.036989 0 -0 0</wrench>
        </link>
      </model>
      <model name='w1'>
        <pose>0 0 0 0 -0 0</pose>
        <link name='Wall_0'>
          <pose>-4.85 -1.02 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='w2'>
        <pose>0.42596 0.36173 0 0 -0 0</pose>
        <link name='Wall_8'>
          <pose>-1.25404 -0.97827 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='w3'>
        <pose>4.11513 0.546959 0 0 -0 0</pose>
        <link name='Wall_20'>
          <pose>2.53913 -0.986211 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='w4'>
        <pose>8.55484 2.18487 0 0 -0 0</pose>
        <link name='Wall_31'>
          <pose>6.30034 -1.1078 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
    </state>
    <gui fullscreen='0'>
      <camera name='user_camera'>
        <pose>6.79966 15.4667 8.53794 4.29577e-18 0.445748 -1.94291</pose>
        <view_controller>orbit</view_controller>
      </camera>
    </gui>
  </world>
</sdf>

"""

f = open("/home/liat/catkin_ws/src/ric_gazebo/worlds/worldRandomized.world", 'w')
f.write(str)
f.close()
