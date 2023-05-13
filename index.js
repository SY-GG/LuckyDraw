const axios = require('axios');

export const handler = async (event) => {
  // TODO implement
  try {
    const result = await axios.post(
      '웹훅url',
      {
        content: '봇 웹훅 테스트 결과',
      }
    );
    console.info('연결 성공');
  } catch (err) {
    console.err('연결 실패', err);
  }
};
