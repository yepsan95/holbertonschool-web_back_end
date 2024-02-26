export default function updateStudentGradeByCity(array, city, newGrades) {
  return array
    .filter((obj) => obj.location === city)
    .map((student) => {
      const studentGrade = newGrades
        .filter((obj) => obj.studentId === student.id)
        .map((x) => x.grade)[0];
      const grade = studentGrade || 'N/A';
      return { ...student, grade };
    });
}
