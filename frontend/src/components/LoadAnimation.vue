<script setup>

</script>

<template>
<div class="loading">
	<div class="heightAuto">
		<h1>Loading pairing... </h1>
		<div id="fountainG">
		<div id="fountainG_1" class="fountainG"></div>
		<div id="fountainG_2" class="fountainG"></div>
		<div id="fountainG_3" class="fountainG"></div>
		<div id="fountainG_4" class="fountainG"></div>
		<div id="fountainG_5" class="fountainG"></div>
		<div id="fountainG_6" class="fountainG"></div>
		<div id="fountainG_7" class="fountainG"></div>
		<div id="fountainG_8" class="fountainG"></div>
		</div>
	</div>
</div>
</template>

<style>
.loading {
  /* width: 80vw;
  height: 85vh; */
  display: flex;
  height: 80vh;
  /* position: relative; */
  /* flex-flow: wrap; */
  flex-direction: column;
  /* align-content: center; */
  justify-content: center;
  /* align-content: center; */
  align-items: center;
  text-align: center;
  /* padding-left: 2vw;
  padding-top: 1vh;
  margin-left: 11vw; */
}

.heightAuto {
  /* height: 100%; */
  margin: 5;
}

.loading h1 {
  margin: 5px;
}

#fountainG{
	position:relative;
	width:180px;
	height:22px;
	margin:auto;
}

.fountainG{
	position:absolute;
	top:0;
	background-color:rgb(153,46,34);
	width:22px;
	height:22px;
	animation-name:bounce_fountainG;
		-o-animation-name:bounce_fountainG;
		-ms-animation-name:bounce_fountainG;
		-webkit-animation-name:bounce_fountainG;
		-moz-animation-name:bounce_fountainG;
	animation-duration:1.5s;
		-o-animation-duration:1.5s;
		-ms-animation-duration:1.5s;
		-webkit-animation-duration:1.5s;
		-moz-animation-duration:1.5s;
	animation-iteration-count:infinite;
		-o-animation-iteration-count:infinite;
		-ms-animation-iteration-count:infinite;
		-webkit-animation-iteration-count:infinite;
		-moz-animation-iteration-count:infinite;
	animation-direction:normal;
		-o-animation-direction:normal;
		-ms-animation-direction:normal;
		-webkit-animation-direction:normal;
		-moz-animation-direction:normal;
	transform:scale(.3);
		-o-transform:scale(.3);
		-ms-transform:scale(.3);
		-webkit-transform:scale(.3);
		-moz-transform:scale(.3);
	border-radius:14px;
		-o-border-radius:14px;
		-ms-border-radius:14px;
		-webkit-border-radius:14px;
		-moz-border-radius:14px;
}

#fountainG_1{
	left:0;
	animation-delay:0.6s;
		-o-animation-delay:0.6s;
		-ms-animation-delay:0.6s;
		-webkit-animation-delay:0.6s;
		-moz-animation-delay:0.6s;
}

#fountainG_2{
	left:22px;
	animation-delay:0.75s;
		-o-animation-delay:0.75s;
		-ms-animation-delay:0.75s;
		-webkit-animation-delay:0.75s;
		-moz-animation-delay:0.75s;
}

#fountainG_3{
	left:45px;
	animation-delay:0.9s;
		-o-animation-delay:0.9s;
		-ms-animation-delay:0.9s;
		-webkit-animation-delay:0.9s;
		-moz-animation-delay:0.9s;
}

#fountainG_4{
	left:67px;
	animation-delay:1.05s;
		-o-animation-delay:1.05s;
		-ms-animation-delay:1.05s;
		-webkit-animation-delay:1.05s;
		-moz-animation-delay:1.05s;
}

#fountainG_5{
	left:90px;
	animation-delay:1.2s;
		-o-animation-delay:1.2s;
		-ms-animation-delay:1.2s;
		-webkit-animation-delay:1.2s;
		-moz-animation-delay:1.2s;
}

#fountainG_6{
	left:112px;
	animation-delay:1.35s;
		-o-animation-delay:1.35s;
		-ms-animation-delay:1.35s;
		-webkit-animation-delay:1.35s;
		-moz-animation-delay:1.35s;
}

#fountainG_7{
	left:135px;
	animation-delay:1.5s;
		-o-animation-delay:1.5s;
		-ms-animation-delay:1.5s;
		-webkit-animation-delay:1.5s;
		-moz-animation-delay:1.5s;
}

#fountainG_8{
	left:157px;
	animation-delay:1.64s;
		-o-animation-delay:1.64s;
		-ms-animation-delay:1.64s;
		-webkit-animation-delay:1.64s;
		-moz-animation-delay:1.64s;
}



@keyframes bounce_fountainG{
	0%{
	transform:scale(1);
		background-color:rgb(153,46,34);
	}

	100%{
	transform:scale(.3);
		background-color:#EAE7DC;
	}
}

@-o-keyframes bounce_fountainG{
	0%{
	-o-transform:scale(1);
		background-color:rgb(153,46,34);
	}

	100%{
	-o-transform:scale(.3);
		background-color:#EAE7DC;
	}
}

@-ms-keyframes bounce_fountainG{
	0%{
	-ms-transform:scale(1);
		background-color:rgb(153,46,34);
	}

	100%{
	-ms-transform:scale(.3);
		background-color:#EAE7DC;
	}
}

@-webkit-keyframes bounce_fountainG{
	0%{
	-webkit-transform:scale(1);
		background-color:rgb(153,46,34);
	}

	100%{
	-webkit-transform:scale(.3);
		background-color:#EAE7DC;
	}
}

@-moz-keyframes bounce_fountainG{
	0%{
	-moz-transform:scale(1);
		background-color:rgb(153,46,34);
	}

	100%{
	-moz-transform:scale(.3);
		background-color:#EAE7DC;
	}
}


</style>