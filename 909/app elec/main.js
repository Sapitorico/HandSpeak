const { app, BrowserWindow } = require('electron')
const { spawn } = require('child_process');
const path = require('path');
const kill = require('tree-kill');

const createWindow = () => {
    const win = new BrowserWindow({
      width: 800,
      height: 600,
    })
  
    win.loadFile('index.html')
  }

app.whenReady().then(() => {
  createWindow()
  const directoryPath = 'C:/Users/5771/Desktop/909/serv';
  const command = 'uvicorn main:app --reload';
  const terminal = spawn(process.platform === 'win32' ? 'cmd.exe' : 'bash', [], {
    cwd: directoryPath,
    shell: true,
  });
  terminal.stdin.write(`${command}\n`)
})

app.on('before-quit', () => {
  if (terminal) {
    kill(terminal.pid);
  }
});

app.on('window-all-closed', () => {
  kill(terminal.pid)
  if (process.platform !== 'darwin') app.quit()
})