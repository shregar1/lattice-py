
import pytest
from utilities.urn import URNUtility

class TestURNUtility:

    def test_utility_instantiation(self) -> None:
        util = URNUtility()
        assert util is not None

    def test_generate_uuid4(self) -> None:
        u_obj = URNUtility.generate_uuid4()
        u_str = URNUtility.generate_uuid4_str()
        assert u_obj is not None
        assert URNUtility.is_valid_uuid(str(u_obj))
        assert URNUtility.is_valid_uuid(u_str)

    def test_generate_transaction_urn(self) -> None:
        txn1 = URNUtility.generate_transaction_urn()
        txn2 = URNUtility.generate_transaction_urn(kind='err')
        assert URNUtility.is_valid_uuid(txn1)
        assert URNUtility.is_valid_uuid(txn2)

    def test_generate_ulid_official_package(self) -> None:
        ulid_str = URNUtility.generate_ulid()
        assert len(ulid_str) == 26
        assert URNUtility.is_valid_ulid(ulid_str)

    def test_generate_nanoid(self) -> None:
        nid1 = URNUtility.generate_nanoid()
        nid2 = URNUtility.generate_nanoid(size=12, alphabet='ABCDEF123456')
        assert len(nid1) == 21
        assert len(nid2) == 12
        assert all((c in 'ABCDEF123456' for c in nid2))

    def test_generate_base62_and_base58(self) -> None:
        b62 = URNUtility.generate_base62(size=16)
        b58 = URNUtility.generate_base58(size=16)
        assert len(b62) == 16
        assert len(b58) == 16

    def test_parse_public_urn_valid(self) -> None:
        valid_uuid = str(URNUtility.generate_uuid4())
        parsed = URNUtility.parse_public_urn(valid_uuid, entity='Candidate')
        assert str(parsed) == valid_uuid

    def test_parse_public_urn_reserved_raises_not_found(self) -> None:
        with pytest.raises(Exception):
            URNUtility.parse_public_urn('me', entity='User')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestURNUtility"

