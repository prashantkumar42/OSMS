isbatch = 0;
isgender = 0;
isaddress = 0;
isfee = 0;
keytype = 1;

function activateSearch() {
    $("#batchContent").hide();
    document.getElementById("studentList").innerHTML = "";
    $("#searchContent").show();
    $("#studentDetails").hide();
    
    document.getElementById("analytics").style = "";
    $("#chartsPane").hide();
    $("#analyticsContent").hide();    

    $("#studentContent").show();

    document.getElementById(highlightedBatch).style = "";
    document.getElementById("search").style = "background-color:darkgreen";
    if (isbatch == 1) {
        document.getElementById("checksbatch").click();
    }
    if (isgender == 1) {
        document.getElementById("checksgender").click();
    }
    if (isaddress == 1) {
        document.getElementById("checksaddress").click();
    }
    if (isfee == 1) {
        document.getElementById("checksfee").click();
    }
}

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
    highlightedSTD = null;
    $("#filterList").slideUp();
    batch = document.getElementById("sbatch").value;
    gender = document.getElementById("sgender").value;
    address = document.getElementById("saddress").value;
    keyword = document.getElementById("searchkey").value;
    endpoint = "/services/search?keyword="+ keyword + "&keytype=" + keytype + "&isbatch=" + isbatch + "&batch=" + batch + "&isgender=" + isgender + "&gender=" + gender + "&isaddress=" + isaddress + "&address=" + address + "&isfee=" + isfee;
    console.log(endpoint);
    var data = null;
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;
    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            students = (JSON.parse(this.responseText)).response;
            if (students.length > 0) {
                $("#studentDetails").show()
                html = "";
                for (i = 0; i < students.length; i++) {
                    html += "<div class='row student' id='student" + students[i].id + "' onclick='viewDetails(" + JSON.stringify(students[i]) + ")'>" + students[i].name + "</div>"; 
                    //console.log(students[i].name);
                }
                //console.log(html);
                document.getElementById("studentSearchResults").innerHTML = html;
                viewDetails(students[0]);
            } else {
                $("#studentDetails").hide()
                document.getElementById("studentSearchResults").innerHTML = "<div class='student' style='background-color:rgb(3,29,52)'>Nothing to show</div>";
            }
        }
    });
    xhr.open("GET", endpoint);
    xhr.send(data);    
}

function showFilters() {
    $("#filterList").slideToggle();
}

$("#filterList").slideToggle();