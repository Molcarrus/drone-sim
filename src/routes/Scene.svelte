<script>
    import { T } from '@threlte/core'
    import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js'
    import { useLoader } from '@threlte/core'
    import { useGltf } from '@threlte/extras'

    const gltf = useLoader(GLTFLoader).load('src/assets/drone.gltf')
</script>

{#if $gltf}
    <T is={($gltf).scene} />
{/if}

<!-- {#await useGltf('/src/assets/scene.gltf') then gltf}
    <T is={gltf.scene} />
{/await} -->