<!DOCTYPE html>
<html lang="en">
<head>
	<?php include "common/head.php" ?>
	<script type="text/javascript" src="scripts/cad.js"></script>
</head>

<body>

<?php include "common/header.php" ?>

<div id="all-content-wrapper">
	<div id="content-wrapper" class="content-sized">
		<div id="content" class="sidebar-or-content">
			<h2 id="content-header">My CAD Work</h2>

			<p>I've taken three CAD courses throughout my time in college. Unfortunately, I don't have any files to 
			show from my Pro-E class at UMass. Below are some examples from the two classes I've taken at USC.</p>

			<h3>AME 408 - Finite Element Analysis (FEA)</h3>
			<p>Advanced modeling:</p>

			<div id="modeling-slideshow" style="text-align: center">
			<?php 
				$width = "500";
				$images = array(
					"images/cad/modeling/funnel.png",
					"images/cad/modeling/funnel detail.png",
					"images/cad/modeling/pump thing.png",
					"images/cad/modeling/pump thing section.png"
				);
				include "features/slideshow.php" ;
			?>
			</div>

			<p>Stress analysis, frequency analysis, and thermal analysis:</p>

			<ul>
				<li>Mesh refinement and result convergence.</li>
				<li>2-D simplifications to improve accuracy and reduce computation time.</li>
			</ul>

			<div id="simulation-slideshow" style="text-align: center">
			<?php 
				$width = "500";
				$images = array(
					"images/cad/simulation/bracket stress.png",
					"images/cad/simulation/spider stress.png",
					"images/cad/simulation/freq analysis 1.png",
					"images/cad/simulation/freq analysis 2.png",
					"images/cad/simulation/pressure vessel.png"
				);
				include "features/slideshow.php";
			?>
			</div>

			<h3>AME 308 - Introduction to SolidWorks and Solid Edge</h3>
			<p>Here is my final project for the SolidWorks part of the course. I modeled my bike.</p>

			<iframe width="960" height="540" src="//www.youtube.com/embed/vKlNvNcNZUc?rel=0" frameborder="0" 
			allowfullscreen></iframe>

			<p>Here is my final project for the Solid Edge part of the course. I modeled an internal combustion
			engine.</p>

			<iframe width="960" height="720" src="//www.youtube.com/embed/i1KYZtsqCKA?rel=0" frameborder="0" 
			allowfullscreen></iframe>

			<p>Note: the bolts on the flywheel don't rotate due to a bug in Solid Edge.</p>
			<p>You can download the part drawings for my Solid Edge project 
			<a href="files/SE Final Project Drawings.pdf" target="_blank">here</a></p>

		</div>
		<div class="after-float"></div>
	</div>
</div>

<?php include "common/footer.php" ?>

</body>
</html>