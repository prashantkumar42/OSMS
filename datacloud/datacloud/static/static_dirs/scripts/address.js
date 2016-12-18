locations = [
    "Street 1, City 1",
    "Street 2, City 1",
    "Street 3, City 1",
    "Street 4, City 1",
    "Street 5, City 1",
    "Street 6, City 1",
    "Street 7, City 1",
    "Street 8, City 1",
    "Street 9, City 1",
    "Street 1, City 2",
    "Street 2, City 2",
    "Street 3, City 2",
    "Street 4, City 2",
    "Street 5, City 2",
    "Street 6, City 2",
    "Street 7, City 2",
    "Street 8, City 2",
    "Street 9, City 2"
]

ahtml = "";
for (var i = 0; i < locations.length; i++) {
   ahtml += "<option>" + locations[i] + "</option>" 
}

document.getElementById("address1").innerHTML = ahtml;
document.getElementById("address2").innerHTML = ahtml;
document.getElementById("uaddress").innerHTML = ahtml;


