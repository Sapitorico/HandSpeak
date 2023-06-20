const { app, BrowserWindow } = require('electron')
const { spawn } = require('child_process');
const path = require('path');
const kill = require('tree-kill');

let terminal 
let isTerminating = false

const createWindow = () => {
    const win = new BrowserWindow({
      width: 800,
      height: 600,
    })
  
    win.loadFile('index.html')
  }

app.whenReady().then(() => {
  const directoryPath = path.join(__dirname, '../../backend_api/modules')
  const command = 'uvicorn main:app';
  terminal = spawn(process.platform === 'win32' ? 'cmd.exe' : 'bash', [], {
    cwd: directoryPath,
    shell: true,
  });
  terminal.stdin.write(`${command}\n`)
  createWindow()
})

app.on('before-quit', (event) => {
  if (!isTerminating) {
    event.preventDefault();
    isTerminating = true;
    kill(terminal.pid, 'SIGTERM', (err) => {
      if (err) {
        console.error('Failed to kill terminal process:', err);
        isTerminating = false;
      } else {
        app.quit();
      }
    });
  }
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})