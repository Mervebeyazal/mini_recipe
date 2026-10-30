describe('SE Primer - karar yolları',()=> {
 for(let n=0;n<8;n++){
  const sequence=[0,1,2].map(i=>((n>>i)&1)?'B':'A');
  it('Yol '+(n+1)+' '+sequence.join(''),()=>{
   cy.visit('/');
   cy.get('[data-testid=start]').click();
   sequence.forEach(option=>{
    cy.get('[data-testid=option-'+option+']').click();
    cy.get('[data-testid=feedback]').should('be.visible');
    cy.get('[data-testid=next]').click();
   });
   cy.contains(sequence.every(x=>x==='A')?'SON A':'SON B').should('be.visible');
   cy.get('[data-testid=restart]').click();
   cy.get('[data-testid=start]').should('be.visible');
  });
 }
 it('Yeni başlayan kişi ipucu görür',()=>{
  cy.visit('/');cy.get('[data-testid=role]').select('tester');
  cy.get('[data-testid=goal]').select('security');
  cy.get('[data-testid=start]').click();
  cy.contains('Test mühendisi olarak').should('be.visible');
  cy.contains('İpucu:').should('be.visible');
 });
 it('Uzman modu 60 saniye ile başlar',()=>{
  cy.visit('/');cy.get('[data-testid=level]').select('expert');
  cy.get('[data-testid=start]').click();
  cy.get('[data-testid=timer]').should('contain','60 SN');
 });
});