function confirmDelete(studentName) {
    return confirm(
        "Are you sure you want to delete " + studentName + "?"
    );
}
function searchStudent() {
    let searchInput = document.getElementById("searchInput");
    let searchText = searchInput.value.toLowerCase();

    let students = document.querySelectorAll(".student-card");

    students.forEach(function(student) {
        let studentName = student.getAttribute("data-name").toLowerCase();

        if (studentName.includes(searchText)) {
            student.style.display = "block";
        } else {
            student.style.display = "none";
        }
    });
}