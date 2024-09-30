from flask import Blueprint

from core.apis import decorators
from core.apis.assignments.schema import AssignmentSchema
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.users import User

principle_assignments_resources = Blueprint('principle_assignments_resources', __name__)



@principle_assignments_resources.route('/principal/assignments', methods=['GET'])
@decorators.authenticate_principal
def list_principal_assignments(p):
    """Lists all submitted and graded assignments for the principal."""
    assignments = Assignment.query.filter(
        (Assignment.state == 'SUBMITTED') | (Assignment.state == 'GRADED')
    ).all()
    assignments_dump = AssignmentSchema().dump(assignments, many=True)
    return APIResponse.respond(data=assignments_dump)

@principle_assignments_resources.route('/principal/teachers', methods=['GET'])
@decorators.authenticate_principal
def list_principal_teachers(p):
    """Lists all teachers for the principal."""
    teachers = User.query.filter_by(role='TEACHER').all()
    teachers_dump = AssignmentSchema().dump(teachers, many=True)
    return APIResponse.respond(data=teachers_dump)

