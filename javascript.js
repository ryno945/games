// Get the table element
var table = document.getElementById("table");

// Add a click event listener to the table headers
table.addEventListener("click", function(event) {
  // Check if the clicked element is a table header
  if (event.target.tagName === "TH") {
    // Get the index of the clicked header
    var index = event.target.cellIndex;
    // Get the order of the sorting (ascending or descending)
    var order = event.target.dataset.order;
    // Toggle the order
    order = order === "asc" ? "desc" : "asc";
    // Set the order attribute
    event.target.dataset.order = order;
    // Sort the table rows by the index and order
    sortTable(table, index, order);
  }
});

// Define a function to sort the table
function sortTable(table, index, order) {
  // Get the table body
  var tbody = table.tBodies[0];
  // Get the table rows
  var rows = Array.from(tbody.rows);
  // Define a compare function
  function compare(a, b) {
    // Get the cell values
    var valA = a.cells[index].textContent;
    var valB = b.cells[index].textContent;
    // Compare the values
    if (valA < valB) {
      return order === "asc" ? -1 : 1;
    } else if (valA > valB) {
      return order === "asc" ? 1 : -1;
    } else {
      return 0;
    }
  }
  // Sort the rows by the compare function
  rows.sort(compare);
  // Remove the existing rows
  while (tbody.firstChild) {
    tbody.removeChild(tbody.firstChild);
  }
  // Append the sorted rows
  for (var row of rows) {
    tbody.appendChild(row);
  }
}
