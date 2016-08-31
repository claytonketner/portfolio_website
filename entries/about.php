<!DOCTYPE html>
<html lang="en">
<head>
	<?php include "common/head.php" ?>
	<link rel="stylesheet" href="style/about.css">
</head>

<body>

<?php include "common/header.php" ?>

<div id="all-content-wrapper">
	<div id="content-wrapper" class="content-sized">
		<div id="content" class="sidebar-or-content">
			<h2 id="content-header">About Me</h2>

			<div id="about-school" class="two-column left">
				<div id="beach-image" class="top-image-wrapper"> 
					<img class="top-image" src='images/about/me david robert on beach.jpg'> 
				</div>

				<h3>School</h3>

				<p>I am a 5th year student at the University of Southern California (USC), about to graduate in May, 
				2014 with a B.S. in Mechanical Engineering and a minor in Computer Science. I am also a member of the
				<a href="http://www.spdalpha.org" target="_blank">Sigma Phi Delta</a> professional Engineering 
				fraternity.</p>

				<p>I chose Mechanical Engineering as my major because of my father. He used to be a metal fabricator and 
				designer before he became the CFO and CTO of my parents' business: 
				<a href="http://www.sanbrunopet.com" target="_blank">San Bruno Pet Hospital</a>. When I was in 
				elementary and middle school, he would bring me in to work and I would see him work and use the huge 
				machines he had. From then on, I've been interested with fabrication, machines, and how things work.</p>

				<p>My decision to minor in Computer Science was caused by my long-running interest and use of 
				programming. The first time I picked up programming was in early-mid middle school. My dad bought me 
				<a href="http://www.simplecodeworks.com/website.html" target="_blank">SiMPLE</a> 
				(still has an awesome website), which I could only run on one of my dad's work computers. 
				I couldn't do much with it, but I've been hooked ever since.</p>
			</div>

			<div id="about-leisure" class="two-column right">
				<div id="young-machine-image" class="top-image-wrapper"> 
					<img class="top-image" src='images/about/young machine.jpg'>
				</div>

				<h3>Leisure</h3>

				<p>When I'm not doing schoolwork (read: never), I enjoy bicycling, snowboarding, spending time with my 
				friends and family, and combining my ME and CS skills by tinkering with robotics and other side 
				projects.</p>

				<div id="snowboard-image"> 
					<?php $width=100; $src="images/about/snowboarding.jpg"; include "features/expanding-image.php" ?> 
				</div>
				<div id="assembly-image"> 
					<?php $width=100; $src="images/about/assembly.jpg"; include "features/expanding-image.php" ?> 
				</div>

				<p>In high school I rowed for the NorCal crew team for three years. My third year, I qualified for the 
				USRowing Youth National Championships in Cincinnati, OH in the lightweight double as stroke seat. 
				My boatmate, Dru, and I finished 8th in the nation!</p>

				<div id="adjusting-image">
					<?php $width=100; $src="images/about/adjusting the boat.jpg"; include "features/expanding-image.php" ?> 
				</div>
				<div id="double-image">
					<?php $width=100; $src="images/about/me jeremy double.jpg"; include "features/expanding-image.php" ?> 
				</div>
				<div id="overhead-image">
					<?php $width=100; $src="images/about/up and overhead.jpg"; include "features/expanding-image.php" ?> 
				</div>

			</div>

			<div class="after-float"></div>

		</div>
		<div class="after-float"></div>
	</div>
</div>

<?php include "common/footer.php" ?>

</body>
</html>