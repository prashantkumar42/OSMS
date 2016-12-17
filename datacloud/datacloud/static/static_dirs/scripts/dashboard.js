function viewDetails(std) {
    //console.log(std);
    document.getElementById("stdName").innerHTML = std.name;
    document.getElementById("stdBatch").innerHTML = (std.batch)[0];
    document.getElementById("stdContact").innerHTML = std.contact;
    document.getElementById("stdFather").innerHTML = std.father;
    document.getElementById("stdMother").innerHTML = std.mother;
    document.getElementById("stdAge").innerHTML = std.age;
    document.getElementById("stdGender").innerHTML = std.gender;
    document.getElementById("stdAddress").innerHTML = std.address;

    document.getElementById("student"+std.id).style = "background-color:rgb(9, 78, 140)";
    if (highlightedSTD != null && highlightedSTD != std.id) {
        document.getElementById("student" + highlightedSTD).style = "";
    }
    highlightedSTD = std.id;
    // create the update and delete buttons
    btnHTML = "<button class='muli btn btn-success' data-toggle='modal' data-target='#updateStudent'>UPDATE INFO</button> <button class='muli btn btn-primary' data-toggle='modal' data-target='#studentFee'>MANAGE FEES</button><button class='pull-right muli btn btn-danger' data-toggle='modal' data-target='#deleteStudent'>DEREGISTER</button>"
    btnDelHTML = "<a href='/services/stddelete?sid=" + std.id + "&bid=" + std.batch + "'><button class='muli btn btn-danger'>Yes, deregister this student !</button></a>"
    document.getElementById("deleteStudentButton").innerHTML = btnDelHTML;
    document.getElementById("udbuttons").innerHTML = btnHTML;
    
    document.getElementById("DelstdName").innerHTML = std.name;
    // fill up the update form
    document.getElementById("uid").value = std.id;
    document.getElementById("uname").value = std.name;
    document.getElementById("ufather").value = std.father;
    document.getElementById("umother").value = std.mother;
    document.getElementById("uage").value = std.age;
    document.getElementById("uaddress").value = std.address;
    document.getElementById("ucontact").value = std.contact;

    var genderDropdown = document.getElementById("ugender");
    for (var i = 0; i < genderDropdown.options.length; i++) {
        var option = genderDropdown.options[i];
        if (option.value == std.gender) {
            option.selected = true;
        } else {
            option.selected = false;
        }
    }

    var batchDropdown = document.getElementById("ubatch");
    for (var i = 0; i < batchDropdown.options.length; i++) {
        var option = batchDropdown.options[i];
        if (option.value == std.batch) {
            option.selected = true;
        } else {
            option.selected = false;
        }
    }

    document.getElementById("studentFeeID").value = std.id;
    document.getElementById("studentFeeBID").value = std.batch;
    if (std.fee === "N") {
        $("#undefined").slideDown();
        $("#updateFeeLabel").hide();
        document.getElementById("installments1").innerHTML = "NA";
        document.getElementById("amount1").innerHTML = "NA";
        document.getElementById("paid1").innerHTML = "NA";
        document.getElementById("installments").value = null;
        document.getElementById("amount").value = null;
        document.getElementById("paid").value = null;

    } else {
        $("#undefined").slideUp();
        document.getElementById("installments1").innerHTML = std.installments;
        document.getElementById("amount1").innerHTML = std.amount;
        document.getElementById("paid1").innerHTML = std.paid;
        document.getElementById("installments").value = std.installments;
        document.getElementById("amount").value = std.amount;
        document.getElementById("paid").value = std.paid;
    }

}

function updateFee() {
    $("#undefined").slideToggle();
}

function getStudents(batchName) {
    //console.log(batchName)
    $("#batchContent").show();
    $("#searchContent").hide();
    document.getElementById("search").style = "";

    endpoint = "/services/api?batch=" + batchName;
    document.getElementById("stdlistname").innerText = "STUDENTS IN " + batchName.toUpperCase();
   
    document.getElementById(batchName).style = "background-color:#666";
    if (highlightedBatch != null && highlightedBatch != batchName) {
        document.getElementById(highlightedBatch).style = "";
    }
    highlightedBatch = batchName;
    highlightedSTD = null;

    var batchDropdown = document.getElementById("ubatch1");
    for (var i = 0; i < batchDropdown.options.length; i++) {
        var option = batchDropdown.options[i];
        if (option.value == batchName) {
            option.selected = true;
        } else {
            option.selected = false;
        }
    }

    document.getElementById("deleteBatchLabel").innerHTML = "<a href='/services/deleteBatch?batch="+ batchName +"' style='color:white'>Yes, I want to delete " + batchName + " batch!</a>"
    document.getElementById("bname").value = batchName;
    document.getElementById("oname").value = batchName;

    // get the data 
    var data = null;
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;
    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            //console.log(this.responseText);
            students = (JSON.parse(this.responseText)).response;
            //console.log(students);
            if (students.length > 0) {
                $("#studentDetails").show()
                html = "";
                for (i = 0; i < students.length; i++) {
                    html += "<div class='row student' id='student" + students[i].id + "' onclick='viewDetails(" + JSON.stringify(students[i]) + ")'>" + students[i].name + "</div>"; 
                    //console.log(students[i].name);
                }
                //console.log(html);
                document.getElementById("studentList").innerHTML = html;
                viewDetails(students[0]);
            } else {
                document.getElementById("studentList").innerHTML = "";
                $("#studentDetails").hide();
            }
        }
    });
    xhr.open("GET", endpoint);
    xhr.send(data);               
}

function getBatches() {
    endpoint = "/services/getBatchNames"
    // get the data 
    var data = null;
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;
    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            console.log(this.responseText);
            batches = (JSON.parse(this.responseText)).response;
            //console.log(students);
            html = ""; ddhtml = "";
            for (i = 0; i < batches.length; i++) {
                html += "<div class='row batch' id='" + batches[i].name + "' onclick='getStudents(\"" + batches[i].name + "\")'>" + batches[i].name + "</div>"; 
                ddhtml += "<option>" + batches[i].name + "</option>"
                //console.log(students[i].name);
            }
            //console.log(html);
            document.getElementById("batchListCol").innerHTML = html;
            document.getElementById("ubatch1").innerHTML = ddhtml;
            document.getElementById("ubatch").innerHTML = ddhtml;
            console.log("sent batch is " + sentBatch)
            if (sentBatch !=  null && sentBatch != "") {
                console.log("doing getStudents for " + sentBatch);
                getStudents(sentBatch); 
            } else {
                if (batches.length > 0) {
                    $("#studentPane").show();
                    console.log("doing getStudents in else for " + batches[0].name);
                    getStudents(batches[0].name);
                } else {
                    $("#studentPane").hide();
                }
            }
        }
    });
    xhr.open("GET", endpoint);
    xhr.send(data);    
}

$("#studentDetails").hide();
getBatches();


function activateSearch() {
    $("#batchContent").hide();
    $("#searchContent").show();
    document.getElementById(highlightedBatch).style = "";
    document.getElementById("search").style = "background-color:black";
}