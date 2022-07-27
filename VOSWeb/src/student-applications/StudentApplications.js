import React from "react";
import { useParams } from "react-router-dom";
function StudentApplications() {
  let params = useParams();

  return (
    <div id="student-applications">
      <label>Place holder for Student Applications {params}</label>
    </div>
  );
}

export default StudentApplications;
