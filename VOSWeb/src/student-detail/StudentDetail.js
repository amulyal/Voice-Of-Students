import React, { useEffect, useState } from "react";
import axios from "axios";
import "./StudentDetail.css";
import { Container, Col, Row } from "react-bootstrap";
import { Link } from "react-router-dom";
function StudentDetail() {
  const [student, setStudentData] = useState({});

  function getStudentData() {
    axios.get("/students/2").then(setData).catch(handleError);
  }

  function setData(response) {
    console.log(response);
    setStudentData(response.data);
  }

  function handleError(error) {
    console.log(error.response.data);
  }

  useEffect(getStudentData);
  return (
    <div id="student-detail">
      <Container>
        <Row>
          <Col sm={2}>First Name:</Col>
          <Col sm={10}>{student.firstName}</Col>
        </Row>
        <Row>
          <Col sm={2}>Last Name: </Col>
          <Col sm={10}>{student.lastName}</Col>
        </Row>
        <Row>
          <Col sm={2}>Email: </Col>
          <Col sm={10}>{student.email}</Col>
        </Row>
        <Row>
          <Col sm={2}>Address:</Col>
          <Col sm={10}>
            {student.address1} {student.address2} {student.city} {student.state}{" "}
            {student.country} {student.pin}{" "}
          </Col>
        </Row>
        <Row>
          <Col sm={2}>Phone Number: </Col>
          <Col sm={10}>{student.phoneNumber} </Col>
        </Row>
        <Row>
          <Col sm={2}>Identification: </Col>
          <Col sm={10}>
            {student.identificationType}-{student.identificationNumber}
          </Col>
        </Row>
        <Row>
          <Col sm={2}>Date of Birth: </Col>
          <Col sm={10}>{student.dateOfBirth} </Col>
        </Row>
        <Row>
          <Col sm={2}>Place of Birth: </Col>
          <Col sm={10}>
            {student.placeOfBirth}-{student.birthCountry}
          </Col>
        </Row>
        <Row>
          <Link to={`/applications/${student.studentId}`} key={student.id}>
            View Applications
          </Link>
        </Row>
      </Container>
    </div>
  );
}

export default StudentDetail;
