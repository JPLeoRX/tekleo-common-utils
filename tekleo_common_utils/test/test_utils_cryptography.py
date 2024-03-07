from tekleo_common_utils.utils_cryptography import UtilsCryptography

utils_cryptography = UtilsCryptography()


class TestUtilsCryptography:
    def test_bcrypt(self):
        p_raw = 'test123'
        p_hashed = utils_cryptography.bcrypt_hash(p_raw)
        print(p_raw, p_hashed)
        print(utils_cryptography.bcrypt_check('test123', p_hashed))
        print(utils_cryptography.bcrypt_check('Test123', p_hashed))

    def test_aes(self):
        a = 'Test123!'
        k = 'D8Ls6Vv7KzPHFWVDzdNeGkNNPr6MJ9Ux'
        print(utils_cryptography.aes_encrypt(a, k))
        print(utils_cryptography.aes_decrypt('hqExCIQdAnDys5/suWDQi69t/lB9hp5AgzUL15uv/J8=', k))