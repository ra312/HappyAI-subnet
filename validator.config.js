module.exports = {
      apps : [{
        name   : 'validator_validator_process',
        script : 'python3',
        cwd    : '/workspace/HappyAI-subnet',
        interpreter: 'none',
        min_uptime: '5m',
        max_restarts: '5',
        args: ['-m', 'app.neurons.validator', '--netuid','103','--subtensor.network','finney','--wallet.name','ckli03','--wallet.hotkey','hkli03','--logging.debug','--blacklist.force_validator_permit','--axon.port','54619'],
        env: {
          PYTHONPATH: '/workspace/HappyAI-subnet'
        }
      }]
    }
