var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value; // Affiche la valeur par défaut de la glissière

// Met à jour la valeur de la glissière à chaque fois qu'on y touche
slider.oninput = function() {
    if(this.value>50){
      output.innerHTML = this.value;
  }
}