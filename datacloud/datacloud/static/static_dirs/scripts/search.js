function activateSearch() {
    $("#batchContent").hide();
    $("#searchContent").show();
    document.getElementById(highlightedBatch).style = "";
    document.getElementById("search").style = "background-color:darkgreen";
}

function search() {
    isbatch = document.getElementById("checksbatch").value;
    batch = document.getElementById("sbatch").value;
    isgender = document.getElementById("checksgender").value;
    gender = document.getElementById("sgender").value;
    isaddress = document.getElementById("checksaddress").value;
    address = document.getElementById("saddress").value;
    isfee = document.getElementById("checksfee").value;
    text = isbatch + " " + batch + " " + isgender + " " + gender + " " + isaddress + " " + address + " " + isfee;
    alert(text);
}

function showFilters() {
    $("#filterList").slideToggle();
}

$("#filterList").slideToggle();