def test_validare_email():
    assert validator_email("test@email.com") == True
    assert validator_email("test@.com") == False
    assert validator_email("") == False
