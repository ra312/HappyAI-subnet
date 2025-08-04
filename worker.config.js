module.exports = {
      apps : [{
        name   : 'validator_worker_process',
        script : 'python3',
        cwd    : '/workspace/HappyAI-subnet/worker',
        interpreter: 'none',
        min_uptime: '5m',
        max_restarts: '5',
        args: ['-m', 'uvicorn', 'app.main:app', '--host', '0.0.0.0', '--port', '1235'],
        env: {
          PYTHONPATH: '/workspace/HappyAI-subnet'
        }
      }]
    }
