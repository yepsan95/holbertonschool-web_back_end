import ClassRoom from './0-classroom.js';
function initializeRooms() {
  let classRoomsArray = [];
  classRoomsArray[0] = new ClassRoom(19);
  classRoomsArray[1] = new ClassRoom(20);
  classRoomsArray[2] = new ClassRoom(34);
  return classRoomsArray;
}
