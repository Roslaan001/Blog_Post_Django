// function typeWriter(element, text, speed) {
//   var i = 0;
//   var txt = text.split("");
//   var speed = speed || 100;

//   function type() {
//     if (i < txt.length) {
//       element.innerHTML += txt[i];
//       i++;
//       setTimeout(type, speed);
//     }
//   }
//   type();
// }

// var typingText = document.getElementById("welcome-message");
// var textToType = typingText.textContent;
// typeWriter(typingText, textToType);