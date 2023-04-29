// // Check if the cookie is set
// if (document.cookie.indexOf("visited=true") != -1) {
//     // The user has visited the site before
//     var confirmLoadPrevInfo = confirm("Would you like to load your previous information?");
  
//     if (confirmLoadPrevInfo) {
//       // Load previous information
//       alert("Loading previous information");
//     } else {
//       // Do not load previous information
//       alert("Loading default content");
//     }
//   } else {
//     // The user has not visited the site before
//     document.cookie = "visited=true; expires=Thu, 1 Jan 2030 00:00:00 UTC; path=/";
//     alert("Loading default content");
//   }
  
document.getElementById('list_name').addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
      submitListName();
    }
  });