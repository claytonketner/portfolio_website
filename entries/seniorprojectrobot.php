<!DOCTYPE html>
<html lang="en">
<head>
	<?php include "common/head.php" ?>
</head>

<body>

<?php include "common/header.php" ?>

<div id="all-content-wrapper">
	<div id="content-wrapper" class="content-sized">
		<div id="content" class="sidebar-or-content">
			<h2 id="content-header">Senior Project Robot</h2> 
			<span id="date">Fall 2012</span><br>
			<a href="#results">Skip to result</a>

			<h3>ASME 2013 Student Design Competition</h3>
			<p>For my senior project class (AME 441) I chose to enter the 
			<a href="http://files.asme.org/asmeorg/Events/Contests/DesignContest/31870.pdf" target="_blank">
			ASME 2013 Student Design Competition</a>. The challenge was to design and build a remote inspection device 
			- inspired by the Fukushima reactor tragedy in Japan. The purpose of this project is to design a robot for 
			inspecting radioactivity levels and damage in a compromised nuclear reactor control room. The robot must be 
			completely remotely controlled and must also have a live video feed because the operator must be in a booth 
			during operation. Groups have only 5 minutes to complete five objectives in the 5 by 7.75 m course. 
			The objectives are as follows:</p>

			<ul>
				<li>Navigate obstacles placed randomly throughout the course</li>
				<li>Read a digital pressure gauge (the operator must be able to read the gauge)</li>
				<li>Push a button located 50 mm up from the ground</li>
				<li>Pick up a 25 mm diameter, 50 mm long wooden rod (simulating a radiation sensor) and drop it off in a designated area</li>
				<li>Pick up another radiation sensor and bring it to the starting location</li>
			</ul>

			<p>For my class, we had to be in groups of 3-4 people, and our projects had to be completed by the end of the semester. 
			The ASME competition deadline is in the spring of 2012, but since I did this as my senior peoject, 
			it had to be completed by December 7, 2012.</p>

			<hr><h3>The Team</h3>
			<p>For this project, I was in a team of four - however, in the beginning, finding people to join was difficult 
			because this project was marked as the highest difficulty of the suggested topics. I instigated this project, 
			and my team members had never worked with programming or electronics any significant amount, so I assigned 
			myself to that part of the project.</p>

			<hr><h3>Wireless Communication Demo</h3>
			<p>Here is a demonstration video of the robot's first movements. This video shows off the wireless communication 
			between the robot and the controller, and also demonstrates the speed and direction control over the DC wheel motors.</p>

			<iframe width="960" height="540" src="//www.youtube.com/embed/DLnoNoAPJco?rel=0" frameborder="0" allowfullscreen></iframe>

			
			<hr><h3 id="results">Video Walkthrough And Demo</h3>
			<p>Notes:</p>

			<ul>
				<li>The robot has its own Arduino and XBee that it uses to drive all of the motors and communicate with the controller.</li>
				<li>The motor driver chip allows the Arduino to drive the DC motors that move the robot. The chip allows for speed and direction control over each motor independently.</li>
				<li>The Arduino cannot put out enough current to drive all of the motors at once, so they are all powered by a 4 AA battery pack (mounted to the top of the robot).</li>
			</ul>

			<iframe width="960" height="540" src="//www.youtube.com/embed/2VCjIk9Rdmw?rel=0" frameborder="0" allowfullscreen></iframe>

		</div>
		<div class="after-float"></div>
	</div>
</div>

<?php include "common/footer.php" ?>

</body>
</html>