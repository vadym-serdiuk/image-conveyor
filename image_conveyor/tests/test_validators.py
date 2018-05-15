from image_conveyor.core.validators import TaskValidator


def test_task_validator_success(task_fixture):
    validator = TaskValidator(task_fixture)
    assert validator.is_valid()


def test_task_validator_empty_error():
    validator = TaskValidator({})
    assert validator.is_valid() == False
    assert "'bucket' is a required property" in validator.errors
    assert "'filename' is a required property" in validator.errors


def test_task_validator_no_bucket_name(task_fixture):
    del task_fixture["bucket"]["name"]
    validator = TaskValidator(task_fixture)
    assert validator.is_valid() == False
    assert "'name' is a required property" in validator.errors
