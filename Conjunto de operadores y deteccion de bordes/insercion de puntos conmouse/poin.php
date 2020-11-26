
<html>

<body>
	<script type="text/javascript" src="click.js"></script>
	
<canvas id="canvas" height="1000px" width="1000px" style="cursor:crosshair;background:url(1.jpg)">

</canvas>

	<div>
	<?php
			$archivo = fopen("puntos.txt", "r");
			$iterator=0;
			while(!feof($archivo)){
				$traer = fgets($archivo);
				$iterator++;
				if($iterator==1)
				{
					$cord=$traer;
				}
		    }
		    echo nl2br($cord);
			fclose($archivo);

	?>
	<script type="text/javascript">
   		 var cord = '<?php echo $cord;?>';
   		 var coordenadas = cord.split(',');
   		 var px1 = parseInt(coordenadas[0]);
   		 var py1 = parseInt(coordenadas[1]);
   		 var px2 = parseInt(coordenadas[2]);
   		 var py2 = parseInt(coordenadas[3]);
   		 var px3 = parseInt(coordenadas[4]);
   		 var py3 = parseInt(coordenadas[5]);
   		 var px4 = parseInt(coordenadas[6]);
   		 var py4 = parseInt(coordenadas[7]);
   		  for(var i=0;i<coordenadas.size();i++){
   		 	console.log(coordenadas);
   		 }
   		 
	</script>
</div>


</body>

</html>