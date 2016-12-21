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
keytype = 1;

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

function searchType(value) {
    keytype = value;
}

function search() {
    batch = document.getElementById("sbatch").value;
    gender = document.getElementById("sgender").value;
    address = document.getElementById("saddress").value;
    keyword = document.getElementById("searchkey").value;
    endpoint = "/services/search?keyword="+ keyword + "&keytype=" + keytype + "&isbatch=" + isbatch + "&batch=" + batch + "&isgender=" + isgender + "&gender=" + gender + "&isaddress=" + isaddress + "&address=" + address + "&isfee=" + isfee;
    console.log(endpoint);
    
}

function showFilters() {
    $("#filterList").slideToggle();
}

$("#filterList").slideToggle();