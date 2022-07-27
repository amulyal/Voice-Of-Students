-- public.student definition

-- Drop table

-- DROP TABLE public.student;

CREATE TABLE public.student (
	student_id int8 NOT NULL GENERATED ALWAYS AS IDENTITY,
	first_name varchar NOT NULL,
	middle_name varchar NULL,
	last_name varchar NOT NULL,
	date_of_birth date NOT NULL,
	nationality varchar NOT NULL,
	birth_city varchar NOT NULL,
	birth_country varchar NOT NULL,
	phone_number varchar NOT NULL,
	email_address varchar NOT NULL,
	address_line_1 varchar NOT NULL,
	address_line_2 varchar NULL,
	city varchar NOT NULL,
	state varchar NOT NULL,
	country varchar NOT NULL,
	pincode int4 NOT NULL,
	national_identification_type varchar NOT NULL,
	national_identification_number varchar NOT NULL,
	date_created timestamp NOT NULL,
	date_modified timestamp NULL,
	CONSTRAINT student_pk PRIMARY KEY (student_id)
);

-- Permissions

ALTER TABLE public.student OWNER TO postgres;
GRANT ALL ON TABLE public.student TO postgres;


-- public.branch definition

-- Drop table

-- DROP TABLE public.branch;

CREATE TABLE public.branch (
	branch_id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	branch_name varchar NOT NULL,
	"degree" varchar NOT NULL,
	duration int4 NOT NULL,
	CONSTRAINT branch_pk PRIMARY KEY (branch_id)
);

-- Permissions

ALTER TABLE public.branch OWNER TO postgres;
GRANT ALL ON TABLE public.branch TO postgres;


-- public.admission_types definition

-- Drop table

-- DROP TABLE public.admission_types;

CREATE TABLE public.admission_types (
	type_id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	type_name varchar NOT NULL,
	CONSTRAINT admission_types_pk PRIMARY KEY (type_id)
);

-- Permissions

ALTER TABLE public.admission_types OWNER TO postgres;
GRANT ALL ON TABLE public.admission_types TO postgres;


-- public.allocation_category definition

-- Drop table

-- DROP TABLE public.allocation_category;

CREATE TABLE public.allocation_category (
	category_id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	category_name varchar NOT NULL,
	CONSTRAINT allocation_category_pk PRIMARY KEY (category_id)
);

-- Permissions

ALTER TABLE public.allocation_category OWNER TO postgres;
GRANT ALL ON TABLE public.allocation_category TO postgres;


-- public.board_type definition

-- Drop table

-- DROP TABLE public.board_type;

CREATE TABLE public.board_type (
	board_id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	board_type varchar NOT NULL,
	CONSTRAINT board_type_pk PRIMARY KEY (board_id)
);

-- Permissions

ALTER TABLE public.board_type OWNER TO postgres;
GRANT ALL ON TABLE public.board_type TO postgres;


-- public.guardian definition

-- Drop table

-- DROP TABLE public.guardian;

CREATE TABLE public.guardian (
	student_id int8 NOT NULL,
	guardian_first_name varchar NOT NULL,
	guardian_middle_name varchar NULL,
	guardian_last_name varchar NOT NULL,
	guardian_contact_number varchar NOT NULL,
	guardian_email_address varchar NULL,
	CONSTRAINT guardian_fk FOREIGN KEY (student_id) REFERENCES public.student(student_id)
);

-- Permissions

ALTER TABLE public.guardian OWNER TO postgres;
GRANT ALL ON TABLE public.guardian TO postgres;


-- public.parent definition

-- Drop table

-- DROP TABLE public.parent;

CREATE TABLE public.parent (
	student_id int8 NOT NULL,
	father_first_name varchar NOT NULL,
	father_middle_name varchar NULL,
	father_last_name varchar NOT NULL,
	mother_first_name varchar NOT NULL,
	mother_middle_name varchar NULL,
	mother_last_name varchar NOT NULL,
	parent_contact_number varchar NOT NULL,
	parent_email_address varchar NOT NULL,
	CONSTRAINT parent_fk FOREIGN KEY (student_id) REFERENCES public.student(student_id)
);

-- Permissions

ALTER TABLE public.parent OWNER TO postgres;
GRANT ALL ON TABLE public.parent TO postgres;


-- public.application definition

-- Drop table

-- DROP TABLE public.application;

CREATE TABLE public.application (
	application_id int8 NOT NULL GENERATED ALWAYS AS IDENTITY,
	student_id int8 NOT NULL,
	board_id int4 NOT NULL, -- 10th board type id
	board_roll_number varchar NOT NULL, -- 10th roll number
	highschool_percentage_marks float4 NULL, -- 10th percentage marks
	highschool_cgpa float4 NULL, -- 10th cgpa
	pu_qualification varchar NOT NULL, -- pu or diploma
	pu_roll_number varchar NOT NULL,
	pu_college_name varchar NOT NULL,
	pu_percentile float4 NULL,
	pu_gpa float4 NULL,
	admission_type_id int4 NOT NULL,
	cet_comedk_id varchar NOT NULL,
	cet_comedk_rank int8 NOT NULL,
	parent_or_guardian bpchar(1) NOT NULL,
	admission_acceptance bpchar(1) NOT NULL,
	year_of_joining int4 NOT NULL,
	branch_id int4 NOT NULL,
	allocation_category_id int4 NOT NULL, -- general or minority
	CONSTRAINT application_pk PRIMARY KEY (application_id),
	CONSTRAINT fk_application_admission_types FOREIGN KEY (admission_type_id) REFERENCES public.admission_types(type_id),
	CONSTRAINT fk_application_allocation_category FOREIGN KEY (allocation_category_id) REFERENCES public.allocation_category(category_id),
	CONSTRAINT fk_application_board FOREIGN KEY (board_id) REFERENCES public.board_type(board_id),
	CONSTRAINT fk_application_branch FOREIGN KEY (branch_id) REFERENCES public.branch(branch_id),
	CONSTRAINT fk_application_student FOREIGN KEY (student_id) REFERENCES public.student(student_id)
);

-- Column comments

COMMENT ON COLUMN public.application.board_id IS '10th board type id';
COMMENT ON COLUMN public.application.board_roll_number IS '10th roll number';
COMMENT ON COLUMN public.application.highschool_percentage_marks IS '10th percentage marks';
COMMENT ON COLUMN public.application.highschool_cgpa IS '10th cgpa';
COMMENT ON COLUMN public.application.pu_qualification IS 'pu or diploma';
COMMENT ON COLUMN public.application.allocation_category_id IS 'general or minority';

-- Permissions

ALTER TABLE public.application OWNER TO postgres;
GRANT ALL ON TABLE public.application TO postgres;