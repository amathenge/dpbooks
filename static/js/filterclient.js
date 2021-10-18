/*

javascript to add a filter button

*/

clientname.addEventListener('input', function() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;

    input = document.getElementById("clientname");

    filter = input.value.toUpperCase().trim();
  
    table = document.getElementById("clients");
    tr = table.getElementsByTagName("tr");

/*
    if (filter == "") {
        // show all lines
        for (i=0; i<tr.length; i++) {
            tr[i].style.display="";
        }
        return;
    }
*/  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
});
