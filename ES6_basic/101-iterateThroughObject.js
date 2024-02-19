export default function iterateThroughObject(reportWithIterator) {
  let result = reportWithIterator[0];
  if (reportWithIterator.length > 1) {
    for (const employee of reportWithIterator.slice(1)) {
      result = result + ' | ' + employee;
    }
  }
  return result;
}
