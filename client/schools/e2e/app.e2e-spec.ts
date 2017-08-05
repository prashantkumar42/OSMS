import { MsschoolsPage } from './app.po';

describe('msschools App', () => {
  let page: MsschoolsPage;

  beforeEach(() => {
    page = new MsschoolsPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});
