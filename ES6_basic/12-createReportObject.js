export default function createReportObject(employeesList) {
  const reportObject = {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments(employeesList) {
      const departmentsList = [...employeesList.keys()];
      return departmentsList.length;
    },
  };
  return reportObject;
}
