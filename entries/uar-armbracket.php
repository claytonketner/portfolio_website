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
			<h2 id="content-header">USC Aerial Robotics Club Arm Bracket</h2> 
			<span id="date">April, 2014</span><br>

			<p>This part attaches to the corners of the base of a quad copter, and holds an arm of the quad. It had to
			be easy to take the arms off so that the quad could easily be transported.</p>

			<h3>Original Design</h3>
			<p>This is the original design that one of the group members came up with:</p>

			<div> 
				<?php $width=80; $src="images/uar arm bracket/original.JPG"; include "features/expanding-image.php" ?> 
			</div>

			<p>The part on the left attaches to the base, the second part slides into the first and twists to prevent it
			from sliding back out, and the part on the right slides into the channel to prevent the second part from
			rotating back and sliding out.</p>

			<p>I immediately identified a few problems with this design. The third part prevents the second part from
			vibrating out, but there isn't anything preventing the third part from coming out. Also, there were no
			clearances, so the parts wouldn't fit together in real life.</p>

			<h3>Redesign</h3>
			<p>I tried to make the original design work, but wasn't having any luck. Because of some problems with the
			way the original part was designed, I decided it would be easier to just recreate the part from scratch.
			I basically just remade the part, but with better editability.</p>

			<p>The major difference between the two designs is that mine uses a threaded cap to hold everything
			together and prevent parts from vibrating off. The problem was that I had never 3D printed threads before. 
			So the first thing to do was see if that was possible. Turns out it was - they worked on the first try!</p>

			<div> 
				<?php $width=80; $src="images/uar arm bracket/thread1.JPG"; include "features/expanding-image.php" ?> 
			</div>
			<div> 
				<?php $width=80; $src="images/uar arm bracket/thread2.JPG"; include "features/expanding-image.php" ?> 
			</div>

			<p>So I put the threads on my redesigned part and printed it:</p>

			<div> 
				<?php $width=80; $src="images/uar arm bracket/printing with threads.JPG"; include "features/expanding-image.php" ?> 
			</div>

			<p>I also edited the part that fits inside the bracket a bit to make it more robust. Here's a slideshow of
			the design:</p>

			<div id="holder-slideshow" style="text-align: center">
				<?php
					$width = "500";
					$images = array(
						"images/uar arm bracket/slideshow 1/IMG_2558.JPG",
						"images/uar arm bracket/slideshow 1/IMG_2564.JPG",
						"images/uar arm bracket/slideshow 1/IMG_2569.JPG",
						"images/uar arm bracket/slideshow 1/IMG_2559.JPG",
						"images/uar arm bracket/slideshow 1/IMG_2560.JPG",
						"images/uar arm bracket/slideshow 1/IMG_2561.JPG",
						"images/uar arm bracket/slideshow 1/IMG_2562.JPG",
						"images/uar arm bracket/slideshow 1/IMG_2565.JPG",
						"images/uar arm bracket/slideshow 1/IMG_2626.JPG",
						"images/uar arm bracket/slideshow 1/IMG_2627.JPG",
						"images/uar arm bracket/slideshow 1/IMG_2628.JPG",
					);
					include "features/slideshow.php";
				?>
			</div>

		</div>
		<div class="after-float"></div>
	</div>
</div>

<?php include "common/footer.php" ?>

</body>
</html>