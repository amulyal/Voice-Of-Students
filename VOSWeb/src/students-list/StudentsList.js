import React, { useEffect, useState } from "react";
import axios from "axios";
import { AgGridColumn, AgGridReact } from "ag-grid-react";
import "ag-grid-community/dist/styles/ag-grid.css";
import "ag-grid-community/dist/styles/ag-theme-alpine.css";

function StudentsList() {
  const [students, setRowData] = useState([]);

  useEffect(() => {
    axios
      .get("/students", {
        crossdomain: true,
      })
      .then((result) => setRowData(result.data));
  }, []);

  return (
    <div id="students-list">
      <div className="ag-theme-alpine" style={{ height: 600, width: 1400 }}>
        <AgGridReact rowData={students}>
          <AgGridColumn field="studentId"></AgGridColumn>
          <AgGridColumn
            field="firstName"
            sortable={true}
            filter={true}
          ></AgGridColumn>
          <AgGridColumn field="lastName"></AgGridColumn>
          <AgGridColumn field="email"></AgGridColumn>
          <AgGridColumn field="address1"></AgGridColumn>
          <AgGridColumn field="city"></AgGridColumn>
          <AgGridColumn field="state"></AgGridColumn>
          <AgGridColumn field="country"></AgGridColumn>
          <AgGridColumn
            field="identificationType"
            sortable={true}
            filter={true}
          ></AgGridColumn>
          <AgGridColumn
            field="identificationNumber"
            sortable={true}
            filter={true}
          ></AgGridColumn>
          <AgGridColumn field="birthCountry"></AgGridColumn>
        </AgGridReact>
      </div>
    </div>
  );
}

export default StudentsList;
