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
    if (highlightedSTD != null) {
        document.getElementById("student" + highlightedSTD).style = "";
    }
    highlightedSTD = std.id;
    // create the update and delete buttons
    btnHTML = "<button class='muli btn btn-success' data-toggle='modal' data-target='#updateStudent'>UPDATE</button> <a href='/services/stddelete?sid=" + std.id + "&bid=" + std.batch + "'><button class='muli pull-right btn btn-danger'>DELETE</button></a>"
    document.getElementById("udbuttons").innerHTML = btnHTML;
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

}


function stdupdate(stdID) {

}


function getStudents(batchID) {
    console.log(batchID)
    batches = ["Learner", "Focus", "Target"];
    endpoint = "/services/api?batch=" + batches[batchID-1];

    document.getElementById("batch"+batchID).style = "background-color:#666";
    if (highlightedBatch != null) {
        document.getElementById("batch" + highlightedBatch).style = "";
    }
    highlightedBatch = batchID;
    highlightedSTD = null;

    // get the data 
    var data = null;
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;
    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            //console.log(this.responseText);
            students = (JSON.parse(this.responseText)).response;
            //console.log(students);
            html = "";
            for (i = 0; i < students.length; i++) {
                html += "<div class='row student' id='student" + students[i].id + "' onclick='viewDetails(" + JSON.stringify(students[i]) + ")'>" + students[i].name + "</div>"; 
                //console.log(students[i].name);
            }
            //console.log(html);
            document.getElementById("studentList").innerHTML = html;
            viewDetails(students[0]);
        }
    });
    xhr.open("GET", endpoint);
    xhr.send(data);               
}

if (sentBatch != null) {
    getStudents(sentBatch); 
} else {
    getStudents(1);
}