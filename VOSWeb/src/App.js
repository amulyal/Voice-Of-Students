import "./App.css";
import { Container, Col, Row } from "react-bootstrap";
import { Link } from "react-router-dom";
//  import StudentDetail from "./student-detail/StudentDetail";
//  import StudentsList from "./students-list/StudentsList";
function App() {
  return (
    <div>
      <Container fluid>
        <nav
          style={{
            borderBottom: "solid 1px",
            paddingBottom: "1rem",
          }}
        >
          <Link to="/students">Student List</Link> |{" "}
          <Link to="/student">Student</Link>|{" "}
          <Link to="/applications">Applications</Link>
        </nav>
        {/* <Row>
          <Col>
            <StudentDetail />
          </Col>
        </Row>
        <Row>
          <Col>
            <StudentsList />
          </Col>
        </Row> */}
      </Container>
    </div>
  );
}

export default App;
