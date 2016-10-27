(function() {

  "use strict";

  var toggles = document.querySelectorAll(".c-hamburger");

  for (var i = toggles.length - 1; i >= 0; i--) {
    var toggle = toggles[i];
    toggleHandler(toggle);
  };

  function toggleHandler(toggle) {
    toggle.addEventListener( "click", function(e) {
      e.preventDefault();
        
	  if(this.classList.contains("is-active") === true){
		  this.classList.remove("is-active");
		  
		  document.getElementById("myNav").style.width = "0%";
	  }
	  else{
		  this.classList.add("is-active")
		  document.getElementById("myNav").style.width = "100%";
	  }
    });
  }
  
	  /* Open when someone clicks on the span element */
	function openNav() {
		document.getElementById("myNav").style.width = "100%";
	}

	/* Close when someone clicks on the "x" symbol inside the overlay */
	function closeNav() {
		document.getElementById("myNav").style.width = "0%";
	}
	
	


})();