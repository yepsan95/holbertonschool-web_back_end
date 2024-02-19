export default function iterateThroughObject(reportWithIterator) {
  const result = reportWithIterator[0]; 
  if (reportWithIterator.length > 1) {
    for (const employee of reportWithIterator.slice(1)) {
      result = result + ' | ' + employee;
    }
  }
  return result;
}
