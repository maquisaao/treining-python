'''
Estudos de Git usando o site https://learngitbranching.js.org/?locale=en_US
'''

git commit -a -m "feat: add new feature"  # Adiciona uma nova funcionalidade
git commit -a -m "fix: correct bug"  # Corrige um bug
git commit -a -m "docs: update documentation"  # Atualiza a documentação   

git checkout -b feature/new-feature  # Cria e muda para uma nova branch
git checkout main  # Volta para a branch principal
git merge feature/new-feature  # Mescla a nova funcionalidade na branch principal

git rebase main  # Rebase da branch atual na branch principal. 

git branch -f main HEAD  # Força a branch main a apontar para o commit atual
git branch -f main HEAD~2  # Força a branch main a apontar para dois commits atrás
git branch -f main c2  # Força a branch main a apontar para o commit c2
git reset --hard HEAD~2  # Reseta o HEAD para dois commits atrás, descartando mudanças

git reset HEAD~2  # Reseta o HEAD para dois commits atrás, mantendo as mudanças (ideal para branches locais)
git revert HEAD~2  # Reverte os últimos dois commits, criando novos commits de reversão (ideal para branches remotas)

git chery-pick c2  # Aplica o commit c2 na branch atual

