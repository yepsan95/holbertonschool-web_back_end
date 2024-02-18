export default function createIteratorObject(report) {
  let result = [];
  for (const employees of Object.values(report.allEmployees)) {
    result = [...employees];
  }

  return result;
}
