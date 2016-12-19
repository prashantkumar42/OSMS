function activateSearch() {
    $("#batchContent").hide();
    $("#searchContent").show();
    document.getElementById(highlightedBatch).style = "";
    document.getElementById("search").style = "background-color:darkgreen";
}

isbatch = 0;
isgender = 0;
isaddress = 0;
isfee = 0;

function toggle_isbatch() {
    isbatch = (isbatch + 1)%2;
}
function toggle_isgender() {
    isgender = (isgender + 1)%2;
}
function toggle_isaddress() {
    isaddress = (isaddress + 1)%2;
}
function toggle_isfee() {
    isfee = (isfee + 1)%2;
}

function search() {
    batch = document.getElementById("sbatch").value;
    gender = document.getElementById("sgender").value;
    address = document.getElementById("saddress").value;
    text = isbatch + " " + batch + " " + isgender + " " + gender + " " + isaddress + " " + address + " " + isfee;
    alert(text);
}

function showFilters() {
    $("#filterList").slideToggle();
}

$("#filterList").slideToggle();