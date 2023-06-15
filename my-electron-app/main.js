const { app, BrowserWindow } = require('electron')
const path = require('path')

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    minWidth: 800,
    minHeight: 600,
    maxWidth: 800,
    maxHeight: 600,
    webPreferences: {
      nodeIntegration: true,
      preload: path.join(__dirname, 'preload.js')
    },
    icon: path.join(__dirname, 'images/s.ico'),
  })

  win.loadFile('index.html')
  win.setMenuBarVisibility(false)

  //this function is EXTREMELY unnecessary, I'm just leaving it here
  //as an example of a more complex form of event registering for later. -Mauricio
  win.webContents.on('will-navigate', (event, url) => {
    if (url.endsWith('education.html')) {
      event.preventDefault();
      win.loadFile('education.html');
    }
  })}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})
