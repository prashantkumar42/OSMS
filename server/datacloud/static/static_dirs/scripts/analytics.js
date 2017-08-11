function activateAnalytics() {
    $("#batchContent").hide();
    document.getElementById("studentList").innerHTML = "";
    $("#searchContent").hide();
    $("#studentDetails").hide();
    $("#studentContent").hide();
    document.getElementById(highlightedBatch).style = "";
    document.getElementById("analytics").style = "background-color:darkgreen";
    document.getElementById("search").style = "";
    $("#chartsPane").show();
    $("#analyticsContent").show();
}